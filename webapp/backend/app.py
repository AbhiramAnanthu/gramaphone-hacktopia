
from flask import Flask,request,render_template,json,jsonify,url_for
from flask_pymongo import PyMongo,MongoClient
from dotenv import load_dotenv
import os
from bson import ObjectId
from flask_cors import CORS
from datetime import datetime

load_dotenv(dotenv_path='.env')
PASSWORD=os.getenv('PASSWORD')

# try:
#     client=MongoClient(PASSWORD)
#     print("Connection successfull")
# except Exception:
#     print("Connection failed")

client=MongoClient('mongodb+srv://aadithyanpramad:Xwwy6TlYeS8wHNbb@cluster0.0uefs.mongodb.net/RD')
app=Flask(__name__)
CORS(app)

db=client["web-app"]
collections_dept=db["Department"]
collections_admin=db["Admin"]
collections_branch=db["Branches"]
collections_works=db["Works"]

#ADMIN
@app.route("/add_admin",methods=["POST"])
def add_admin():
    data=request.json
    Admin_name=data["Admin_name"]
    Admin_address=data["Admin_address"]
    Admin_department=data["Admin_department"]
    Admin_email=data["Admin_email"]
    Admin_phone=data["Admin_phone"]
    if Admin_name and Admin_department and Admin_address and Admin_email and Admin_phone and request.method=="POST":
        collections_admin.insert_one(data)
        return jsonify("Data successfully entered"),200
    else:
        return jsonify("Failed to enter data"),404

@app.route("/read_admin/<email_id>",methods=["GET"])
def read_admin(email_id):
    check=collections_admin.find_one({"Admin_email":email_id})
    if check:
        check["_id"]=str(check["_id"])
        admin_list={"Admin_name":check["Admin_name"],"Admin_address":check["Admin_address"],"Admin_department":check["Admin_department"],"Admin_email":check["Admin_email"],"Admin_phone":check["Admin_phone"]}
        return jsonify(admin_list)
    else:
        return jsonify("Couldn't find admin"),404

#DEPARTMENTS
@app.route("/add_dep",methods=["POST"])
def add_dep():
    data = request.json
    department_name = data["Department_name"]
    address = data["Address"]
    branches = data["Branches"]
    district = data["District"]
    current_dept_admin = data["Current_Dept_Admin"]
    head_of_dept = data["Head_of_Dept"]
    hod_phone = data["HOD_Phone"]
    hod_email = data["HOD_Email"]
    

    if department_name and address and branches and district and current_dept_admin and head_of_dept and hod_phone and hod_email and request.method=="POST":
        collections_dept.insert_one(data)
        return jsonify("The data has been inserted"),200
    else:
        return jsonify("The insertion has failed"),404

@app.route("/read_dep/",methods=["GET"])
def read_def():
    read=collections_dept.find()
    dept_list=[{"Department_name":reads["Department_name"],"Address":reads["Address"],"Branches":reads["Branches"],"District":reads["District"],"Current_Dept_Admin":reads["Current_Dept_Admin"],"Head_of_Dept":reads["Head_of_Dept"],"HOD_Phone":reads["HOD_Phone"],"HOD_Email":reads["HOD_Email"]}for reads in read]
    return jsonify(dept_list)

#BRANCHES
# @app.route("/add_branch",methods=["POST"])
# def add_branch():
#     data = request.json
#     Branch_name = data["Branch_name"]
#     Branch_address = data["Branch_address"]
#     Phone_numbers = data["Phone_numbers"]
#     Calls_per_hour = data["Calls_per_hour"]
#     Resolved_works = data["Resolved_works"]
#     Unresolved_works = data["Unresolved_works"]
#     Underresolved_works = data["Underresolved_works"]
#     Officers = data["Officers"]
#     Head_of_branch = data["Head_of_branch"]

#     if Branch_address and Branch_name and Phone_numbers and Calls_per_hour and Resolved_works and Unresolved_works and Underresolved_works and Officers and Head_of_branch and request.method=="POST":
#         collections_branch.insert_one(data)
#         return jsonify("Data added successfully"),200
#     else:
#         return jsonify("Failed to add data"),404
    
# @app.route("/read_branch",methods=["GET"])
# def read_branch():
#     read=collections_branch.find()
#     branch_list=[{"Branch"}]



db = client['web-app']
officer_collection = db['Officers']
work_collection = db["Works"]
applicant_collection = db["Applicant"]


#OFFICERS
@app.route('/officers', methods=['POST'])
def create_officer():
    data = request.json
    name = data["Name"]
    address = data["Address"]
    department = data["Department"]
    email = data["Email"]
    office_address = ["Office_Address"]
    branch_name = ["Branch_Name"]
    position = data["Position"]
    phone_number=data["Phone_Number"]
    officer_collection.insert_one(data)
    
    return jsonify({"message": "User added successfully!"}), 201


@app.route("/officers/<email_id>", methods=['GET'])
def getOfficerDetails(email_id):
    officer=officer_collection.find_one({"Email":email_id})

    if officer:
        officer["_id"]=str(officer["_id"])

        list={
            "ID":officer["_id"],
            "Name":officer["Name"],
            "Address":officer["Address"],
            "Office_Address":officer["Office_Address"],
            "Position":officer["Position"],
            "Email":officer["Email"],
            "Phone_Number":officer["Phone_Number"]
        }

        return jsonify(list)
    else:
        return jsonify({"message":"Officer not found"}),404

# WORKS
@app.route("/add_work",methods=["POST"])
def add_work():
    data=request.json
    Work_title=data["Work_title"]
    Applicant_details=data["Applicant_details"]
    Work_description=data["Work_description"]
    Updates=data["Updates"]
    Officer_to_serve=data["Officer_to_serve"]
    Department=data["Department"]
    Created_at=datetime.now()

    if Work_description and Work_title and Applicant_details and Department and Officer_to_serve and Updates and request.method=="POST":

        documents={
            "Work_title":Work_title,
            "Applicant_details":Applicant_details,
            "Work_description":Work_description,
            "Updates":Updates,
            "Created_at":Created_at,
            "Officer_to_serve":Officer_to_serve,
            "Department":Department
        }
        collections_works.insert_one(documents)
        return jsonify("Data inserted successfully"),200
    else:
        return jsonify("Failed to insert data"),404

@app.route("/read_work/<id>",methods=["GET"])
def read_work(id):
    user=collections_works.find_one({"Officer_to_serve":id})

    if user:
        user["_id"]=str(user["_id"])

        list={
                "Work_title":user["Work_title"],
                "Applicant_details":user["Applicant_details"],
                "Work_description":user["Work_description"],
                "Updates":user["Updates"],
                "Created_at":user["Created_at"],
                "Officer_to_serve":user["Officer_to_serve"],
                "Department":user["Department"]
            }
        return jsonify(list)
    else:
        return jsonify({"message":"Couldn't find officer"})



@app.route("/get_applicants/<applicant_id>",methods=['GET'])
def getApplicants(applicant_id):
    applicant = applicant_collection.find_one({"_id": ObjectId(applicant_id)})
    if applicant:
        applicant["_id"] = str(applicant["_id"])
        return jsonify(applicant)
    return jsonify({"message": "Applicant not found!"}), 404


if __name__ == "__main__":
  app.run(debug=True)

