# message: add delete and list 
import os


FILE = "messages.txt"

def load_messages():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_messages(messages):
    with open(FILE, "w") as file:
        for msg in messages:
            file.write(msg + "\n")



def Add_Message(msg):
    messages = load_messages()
    messages.append(msg)
    save_messages(messages)
    print(f"'{msg}' has been added.")


def Delete_Message(msg):
    messages = load_messages()
    if msg in messages:
        messages.remove(msg)
        save_messages(messages)
        print(f"'{msg}' has been deleted.")
    else:
        print(f"'{msg}' is not present")


def List_Messages():
    messages = load_messages()
    if messages:
        print("\nList of messages:")
        for msg in messages:
            print(f"{msg}")
    else:
        print("No messages.")


def Menu():
    print("\nOperation to be done on the messages:")
    print("1.Add a message")
    print("2.Delete a message")
    print("3.List messages")
    print("4.Exit")




def main():
    while True:
        Menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            messages = input("Enter message:")
            Add_Message(messages)
        elif choice == '2':
            msg = input("Entet message to be deleted:")
            Delete_Message(msg)
        elif choice == '3':
            List_Messages()
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Invalid choice,try again.")


if __name__ == "__main__":
    main()

