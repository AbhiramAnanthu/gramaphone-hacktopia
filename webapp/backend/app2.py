from flask import Flask,request,render_template,json,jsonify,url_for
import pymongo
from dotenv import load_dotenv
import os
from bson import ObjectId
from flask_cors import CORS


load_dotenv(dotenv_path='.env')
PASSWORD=os.getenv('PASSWORD')

app = Flask(__name__)

try:
    client=pymongo.MongoClient(PASSWORD)
    print("Connection successfull")
except Exception:
    print("Connection failed")

db = client['web-app']
applicant_collection = db["Applicant"]

@app.route("/create_applicants",methods=['GET','POST'])
def createApplicants():
    data = request.json
    name = data["Name"]
    aadhar_number = data["Aadhar_Number"]
    phone_number=data["Phone_Number"]
    call_history = data["Call_History"] 
    scheduled_calls_recent = data["Scheduled_Calls_Recent"]  
    scheduled_message_recent = data["Scheduled_Message_Recent"] 
    applicant_data = {
        "Name": name,
        "Aadhar_Number": aadhar_number,
        "Phone_Number": phone_number,
        "Call_History": call_history,
        "Scheduled_Calls_Recent": scheduled_calls_recent,
        "Scheduled_Message_Recent": scheduled_message_recent
    }
    applicant_collection.insert_one(data)
    return jsonify({"message": "Applicant added successfully!"}), 201



if __name__ =="__main__":
    app.run(debug=True)