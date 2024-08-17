import requests
import json
Token = {}

def main_menu():
    print("\nMain Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def message_menu():
    print("4. Logout")


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
        if response != None:
            print(response.json())
        
        
def Login():
    global Token
    url = "http://localhost:5000/Login"
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    payload = {
        "username": username,
        "password": password
    }
    
    response = requests.post(url, json= payload)
    if response.status_code == 200:
        Token = response.json()
        print("User Logged in succesfully")
        Choose_Users()
        return(True) 
    return(False)


    
def Choose_Users():
    i = 1
    url = "http://localhost:5000/Users"
    response = requests.get(url)
    Python_List = json.loads(response.content)
    for p in Python_List:
        print(i, ":", p)
        i += 1
    print("Whom do you want to communicate with?")
    c = int(input())
    c = c-1   
    print(Python_List[c])

    


def Send_Message(msg):
    global Token
    # Reciever = 'users.json'
    print(Token)
    url = "http://localhost:5000/messages"
    payload = {"To": "Python_List[c]", "Token": Token, "Message": msg}
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print(response.json())


def List_Messages():
    url = "http://localhost:5000/messages"
    payload = {"Token": Token}
    response = requests.get(url, json=payload)
    if response.status_code == 200:
        print(json.dumps(response.json() , indent=4))



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
        # else:
        #     message_menu()
        #     choice = input("Choose an option (1-4): ")
        #     if choice == '1':
        #         messages = input("Enter message:")
        #         Send_Message(messages)
        #     elif choice == '2':
        #         List_Messages()
        #     elif choice == '3':
        #         List_Users()
        #     elif choice == '4':
        #         print("Exit")
        #         break
        # else:
        #     print("Invalid choice,try again.")



if __name__ == "__main__":
    main()


