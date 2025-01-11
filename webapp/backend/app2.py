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

@app.route("/get_applicants/<applicant_id>",methods=['GET'])
def getApplicants(applicant_id):
    applicant = applicant_collection.find_one({"_id": ObjectId(applicant_id)})
    if applicant:
        applicant["_id"] = str(applicant["_id"])
        return jsonify(applicant)
    return jsonify({"message": "Applicant not found!"}), 404



if __name__ =="__main__":
    app.run(debug=True)