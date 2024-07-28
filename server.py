from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
import os
import json
import secrets
import string

MESSAGES_FILE = "messages.json"
USERS_FILE = "Users.json"
app = Flask("d")



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


def generate_register_id(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
                   

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(Users):
    with open(USERS_FILE, "w") as file:
        json.dump(Users, file)


def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, "r") as file:
            data = json.load(file)
            return data
    return []

def save_messages(messages):
    with open(MESSAGES_FILE, "w") as file:
        json.dump(messages,file)



@app.route("/Register",methods = ['POST'])
def Register():
    data = request.json
    Users  = load_users()
    RegisterID = generate_register_id()
    data["RegisterID"] = RegisterID
    Users.append(data)
    save_users(Users)
    return jsonify("User Registered Succesfully") , 201


@app.route("/Users",methods = ['GET'])
def List_Users():
    Users = load_users()
    return Users , 200


@app.route("/Login",methods = ['POST'])
def Login():
    data = request.json
    x = load_users()
    for User_entry  in x:
        if User_entry["username"]  ==  data["username"]:
            if User_entry["password"]==  data["password"]:
                
                return Token_get(User_entry['RegisterID']) , 200
            else:
                return jsonify("Wrong Password"), 404
    else:
        return jsonify("Invalid User"), 404
    
    

@app.route("/messages",methods = ['POST'])
def Add_Message():
    data = request.json
    messages = load_messages()
    messages.append(data)
    save_messages(messages)
    return jsonify("Message has been added.") , 201
    


@app.route("/messages",methods = ['GET'])
def List_Messages():
    messages = load_messages()
    return messages , 200
