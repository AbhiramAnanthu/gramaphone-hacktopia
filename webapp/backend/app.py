<<<<<<< Updated upstream
from flask import Flask,request,render_template,json,jsonify,url_for
from flask_pymongo import PyMongo,MongoClient
from dotenv import load_dotenv
import os
from bson import ObjectId
from flask_cors import CORS

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

@app.route("/read_admin",methods=["GET"])
def read_admin():
    read=collections_admin.find()
    admin_list=[{"Admin_name":reads["Admin_name"],"Admin_address":reads["Admin_address"],"Admin_department":reads["Admin_department"],"Admin_email":reads["Admin_email"],"Admin_phone":reads["Admin_phone"]} for reads in read]
    return jsonify(admin_list)

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
@app.route("/add_branch",methods=["POST"])
def add_branch():
    data = request.json
    Branch_name = data["Branch_name"]
    Branch_address = data["Branch_address"]
    Phone_numbers = data["Phone_numbers"]
    Calls_per_hour = data["Calls_per_hour"]
    Resolved_works = data["Resolved_works"]
    Unresolved_works = data["Unresolved_works"]
    Underresolved_works = data["Underresolved_works"]
    Officers = data["Officers"]
    Head_of_branch = data["Head_of_branch"]

    if Branch_address and Branch_name and Phone_numbers and Calls_per_hour and Resolved_works and Unresolved_works and Underresolved_works and Officers and Head_of_branch and request.method=="POST":
        collections_branch.insert_one(data)
        return jsonify("Data added successfully"),200
    else:
        return jsonify("Failed to add data"),404

    





if __name__=="__main__":
    app.run(debug=True)

=======
from flask import Flask,request,jsonify
import pymongo
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv(dotenv_path=".env")
PASSWORD = os.getenv("MONGODB")
print(PASSWORD)
app = Flask(__name__)
CORS(app)

try:
  client=pymongo.MongoClient(PASSWORD)
  print("Connected Successfully!!")
except Exception as e:
  print("Connection Failed")


db = client['web-app']
officer_collection = db['Officers']
work_collection = db["Works"]
applicant_collection = db["Applicant"]



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


@app.route("/officers/<officer_id>", methods=['GET'])
def getOfficerDetails(officer_id):
   
    user = officer_collection.find_one({"_id": ObjectId(officer_id)})
    
    if user:
      
        user["_id"] = str(user["_id"])
        
        return jsonify({
            "Office_Address": user["Office_Address"],
            "Branch_Name": user["Branch_Name"],
            "Position": user["Position"]
        })
    
    return jsonify({"message": "User not found!"}), 404

if __name__ == "__main__":
  app.run(debug=True)
>>>>>>> Stashed changes
