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
        return jsonify("User Added Succesfully") , 201


@app.route("/Users",methods = ['GET'])
def List_Users():
    User = list(collection2.find({}))
    return jsonify(User) , 200


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
    x = collection2.find_one({"username": data["username"]})
    for User_entry  in x:
        if User_entry["password"] ==  data["password"]:        
            return Token_get(User_entry['RegisterID']) , 200
        else:
            return jsonify("Wrong Password"), 404
    else:
        return jsonify("Invalid User"), 404
    
    

# @app.route("/messages",methods = ['POST'])
# def Add_Message():
#     data = request.json
#     messages = load_messages()
#     messages.append(data)
#     save_messages(messages)
#     return jsonify("Message has been added.") , 201
    


# @app.route("/messages",methods = ['GET'])
# def List_Messages():
#     messages = load_messages()
#     return messages , 200




