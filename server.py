import os
import json
from flask import Flask ,request, jsonify



FILE = "messages.txt"
app = Flask("d")

def load_messages():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            data = json.load(file)
            return data
    return []

def save_messages(messages):
    with open(FILE, "w") as file:
        json.dump(messages,file)


@app.route("/messages",methods = ['POST'])
def Add_Message():
    data = request.json
    messages = load_messages()
    messages.append(data)
    save_messages(messages)
    return jsonify("Message has been added.") , 201
    


def List_Messages():
    messages = load_messages()
    if messages:
        print("\nList of messages:")
        for msg in messages:
            print(f"{msg}")
    else:
        print("No messages.")

