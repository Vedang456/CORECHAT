from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
import secrets
import string
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['Chat_Application']
collection1 = db['Messages']
collection2 = db['Users']

app = Flask("d")


def generate_register_id(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
                   


@app.route("/Register",methods = ['POST'])
def Register():
    data = request.json
    RegisterID = generate_register_id()
    data["RegisterID"] = RegisterID
    existing_user = collection2.find_one({"username": data["username"]})
    print(existing_user)
    if existing_user:
        return "This user already exists" , 409
    else:
        y = collection2.insert_one(data)
        return jsonify("Added Succesfully") , 201


@app.route("/Users",methods = ['GET'])
def List_Users():
    Printable_Users = []
    Users = list(collection2.find({},{"username": 1}))
    for u in Users:
        Printable_Users.append(u["username"])
    return Printable_Users, 200


def Token_get(RegisterID):
    current_time = datetime.now(timezone.utc)
    var = current_time.strftime("%Y-%m-%d %H:%M:%S")
    expiry_time = (current_time + timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
    Token = {
        "TokenIssued": var,
        "TokenExpiry": expiry_time,
        "RegisterID": RegisterID
    }
    return Token


@app.route("/Login",methods = ['POST'])
def Login():
    data = request.json
    User_entry = collection2.find_one({"username": data["username"]})
    if User_entry != None:
        if User_entry["password"] ==  data["password"]:        
            return Token_get(User_entry['RegisterID']) , 200
        else:
            return jsonify("Wrong Password"), 404
    else:
        return jsonify("Invalid User"), 404
    
    

@app.route("/messages",methods = ['POST'])
def Send_Message():
    data = request.json
    Token = data["Token"]
    From_User = collection2.find_one({"RegisterID": Token["RegisterID"]})
    To_User = collection2.find_one({"username": data["User"]})
    print(To_User)
    print(From_User)
    if To_User != None and From_User != None:
        record = {
                    "To": To_User["username"],
                    "From": From_User["username"],
                    "Message": data["Message"]
        }
        x = collection1.insert_one(record)
        return jsonify("Message has been sent.") , 201
    else: 
        return("L"), 404
    


@app.route("/messages",methods = ['GET'])
def List_Messages():
    Printable_Messages = []
    Messages = list(collection1.find({},{"_id":0}))
    for m in Messages:
        Printable_Messages.append(m)
    return Printable_Messages, 200
    







