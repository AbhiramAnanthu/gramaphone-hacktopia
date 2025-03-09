import os
import base64
import json
import pyaudio
import audioop
from pyaudio import PyAudio
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.websockets import WebSocketDisconnect
from twilio.twiml.voice_response import VoiceResponse, Connect, Say, Stream
from vosk import KaldiRecognizer, Model
from boto3 import client
from llm import converse_ai, update_database

import pymongo

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
FRAMED_PER_BUFFER = 3200

app = FastAPI()
model_path = "models/vosk-model-en-in-0.5"
model = Model(model_path=model_path)
recognizer = KaldiRecognizer(model, RATE)

polly = client(
    "polly",
    region_name="us-east-1",
    aws_access_key_id=os.getenv("POLLY_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("POLLY_SECRET_ACCESS"),
)


@app.get("/", response_class=JSONResponse)
async def index_page():
    return {"message": "Twilio media stream server is running"}


@app.api_route("/incoming-call", methods=["GET", "POST"])
async def handle_incoming_call(request: Request):
    response = VoiceResponse()
    response.say("Your voice is streamed to an external server.")
    response.pause(lenght=1)
    host = request.url.hostname
    connect = Connect()
    connect.stream(url=f"wss://{host}/media-stream")
    response.append(connect)

    return HTMLResponse(str(response), media_type="application/xml")


@app.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
    print("Client connected")

    complaints = []
    await websocket.accept()
    try:
        async for message in websocket.iter_text():
            data = json.loads(message)
            if data["event"] == "start":
                stream_sid = data["start"]["streamSid"]
                print(f"Incoming stream has started {stream_sid}")
            elif data["event"] == "media":
                payload = data["media"]["payload"]
                audio_decoded = base64.b64decode(payload)
                pcm_data = audioop.ulaw2lin(audio_decoded, 2)
                if recognizer.AcceptWaveform(pcm_data):
                    input_transcript = json.loads(recognizer.Result())
                    if input_transcript["text"] != "":
                        prompt = input_transcript["text"]
                        send_data = {"prompt": prompt, "disconnected": False}
                        response_llm_text = converse_ai(send_data)
                        complaints.append(send_data["prompt"])
                        response_speech = polly.synthesize_speech(
                            Text=response_llm_text,
                            OutputFormat="pcm",
                            VoiceId="Joanna",
                            SampleRate="8000",
                        )
                        if "AudioStream" in response_speech:
                            pcm_data = response_speech["AudioStream"].read()
                            sample_width = 2
                            mulaw_data = audioop.lin2ulaw(pcm_data, sample_width)

                            base64_audio = base64.b64encode(mulaw_data).decode("utf-8")
                            response_data = {
                                "event": "media",
                                "streamSid": stream_sid,
                                "media": {"payload": base64_audio},
                            }

                            await websocket.send_json(response_data)
            else:
                if len(complaints) > 0:
                    response = update_database(complaints)
                    print(response)
    except WebSocketDisconnect as e:
        print("Websocket disconnected")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050)
