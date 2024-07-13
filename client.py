import requests
import json
from time import strftime ,gmtime

FILE = "messages.txt"

def Menu():
    print("\nOperation to be done on the messages:")
    print("1.Add a message")
    print("2.Delete a message")
    print("3.List messages")
    print("4.Exit")



def current_time():
    var = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return(var)


def Add_Message(msg):
    url = "http://localhost:5000/messages"
    payload = {"To": "Maguu","From": "Gaguu", "Message": msg}
    response = requests.post(url, json=payload)
    print(response.json())


def main():
    while True:
        Menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            messages = input("Enter message:")
            Add_Message(messages)
        # elif choice == '2':
        #     msg = input("Entet message to be deleted:")
        #     #Delete_Message(msg)
        # elif choice == '3':
        #     #List_Messages()
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Invalid choice,try again.")



if __name__ == "__main__":
    main()


