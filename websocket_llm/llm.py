from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import add_messages
from langgraph.graph import StateGraph, START, END

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

# Initialize embeddings, LLM, Pinecone, and vector store
embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("gramaphone-index")
vector_store = PineconeVectorStore(
    index=index, embedding=embedding, pinecone_api_key=os.getenv("PINECONE_API_KEY")
)

chat_history = []


class State(TypedDict):
    messages: Annotated[list, add_messages]


from pydantic import BaseModel, Field


class ComplaintExtractor(BaseModel):
    """Extract the complaint details from the user"""

    name: str = Field(description="Extract the name from the user")
    age: str = Field(description="Extract the age of the user")
    dob: str = Field(description="Extract the date of birth of the user")
    aadharnumber: str = Field(description="Extract the Aadhar number of the user")
    complaint_summary: str = Field(
        description="Extract the complaint summary from the user"
    )
    complaint_title: str = Field(description="Title of the complaint")


chat_history = []

import pymongo

client = pymongo.MongoClient(os.getenv("MONGODB"))
db = client["web-app"]
collection = db["Works"]


def converse_ai(message: dict):
    """
    Handles the conversation for complaint registration.
    If the user disconnects, extracts all human messages, summarizes the complaint,
    and collects the data in a ComplaintExtractor object to store it in the database.
    """
    complaint_record = []

    if not message["disconnected"]:
        system_prompt = (
            " You are a realtime AI assistant for complaint registrations."
            " Collect basic details of the user -> name, age, dob, Aadhaar,location"
            " You work for a single Gramapanchayath. Extract the complaint from the conversation."
            " At the end of the conversation, thank the user for complaining and assure them that"
            " you will forward their complaint shortly."
            " Always answer in one or two sentences."
            "Don't repeat questions"
        )

        # Create a prompt template with the chat history
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # Generate response
        chain = qa_prompt | llm
        response = chain.invoke(
            {"input": message["prompt"], "chat_history": chat_history}
        )

        complaint_record.append(message["prompt"])
        # Extend chat history with human and AI messages
        chat_history.extend(
            [
                HumanMessage(content=message["prompt"]),
                AIMessage(content=response.content),
            ]
        )

        return response.content


def update_database(complaint_record: list):
    combined_complaint = " ".join(complaint_record)

    extraction_prompt = (
        ChatPromptTemplate.from_template(
            """
            Using the following combined complaint text, extract the details as follows:
            - Name
            - Age
            - Date of Birth (DOB)
            - Aadhaar Number
            - Complaint Summary
            - location(city)

            Input: {context}
            """
        )
        | llm.with_structured_output(schema=ComplaintExtractor)
    )

    complaint_data = extraction_prompt.invoke({"context": combined_complaint})

    insert_data = {
        "work-title": complaint_data.complaint_title,
        "applicant-details": {
            "name": complaint_data.name,
            "aadharnumber": complaint_data.aadharnumber,
        },
        "work-description": complaint_data.complaint_summary,
        
    }

    complaint_json = complaint_data.dict()
    collection.insert_one(complaint_json)

    print("Complaint saved to database:", complaint_json)

    return "Complaint registered successfully. Thank you for reaching out!"
