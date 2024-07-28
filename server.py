from flask import Flask, request, jsonify, render_template
import os
import json

MESSAGES_FILE = "messages.txt"
USERS_FILE = "Users.txt"
app = Flask("d")

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
    Users.append(data)
    save_users(Users)
    return jsonify("User Registered Succesfully") , 201


@app.route("/Users",methods = ['GET'])
def List_Users():
    Users = load_users()
    return Users , 200



@app.route("/Login",methods = ['POST'])
def Login():
    return jsonify("User logged in") , 201
    

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

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)
