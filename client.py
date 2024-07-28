import requests
import json


def main_menu():
    print("\nMain Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def message_menu():
    print("\nMessage Menu:")
    print("1. Add a message")
    print("2. List Messages")
    print("3. List Users")
    print("4. Logout")


def Add_Message(msg):
    url = "http://localhost:5000/messages"
    payload = {"To": "Maguu","From": "Gaguu", "Message": msg}
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print(response.json())


def List_Messages():
    url = "http://localhost:5000/messages"
    response = requests.get(url)
    if response.status_code == 200:
        print(json.dumps(response.json() , indent=4))


def Register():
    url = "http://localhost:5000/Register"
    print("Please provide the Following information")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    email = input("Email: ").strip()

    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "email": email
    }

    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print(response.json())
    
def List_Users():
    url = "http://localhost:5000/Users"
    response = requests.get(url)
    print(json.dumps(response.json(), indent=4))

    
 
def Login():
    url = "http://localhost:5000/Login"
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    payload = {
        "username": username,
        "password": password
    }
    
    response = requests.post(url, json= payload)
    if response.status_code == 200:
         with open('Login.json', "w") as file:
            json.dump(response.json(),file)
            print("User Logged in succesfully")
            return(True) 
    return(False)




def main():
    logged_in = False
    while True:
        if not logged_in:
            main_menu()
            choice = input("Choose an option (1-3): ")
            if choice == '1':
                Register()
            elif choice == '2':
                logged_in = Login()
            elif choice == '3':
                print("Exit")
                break
            else:
                print("Invalid choice, try again.")
        else:
            message_menu()
            choice = input("Choose an option (1-4): ")
            if choice == '1':
                messages = input("Enter message:")
                Add_Message(messages)
            elif choice == '2':
                List_Messages()
            elif choice == '3':
                List_Users()
            elif choice == '4':
                print("Exit")
                break
            else:
                print("Invalid choice,try again.")



if __name__ == "__main__":
    main()


