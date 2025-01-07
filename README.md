
---

# **CoreChat - A Simple Chat Application**

CoreChat is a basic chat application built with Python, Flask, and MongoDB. This application allows users to register, log in, and exchange messages in real-time. It is a simple, yet effective project to demonstrate my skills in web development, databases, and API integration.
This is v1 of CoreChat , i.e Without frontend and Delete message API which will be added in later versions.

---

## **Features**

- **User Registration**: Allows new users to create accounts with unique usernames and passwords.
- **User Login**: Authenticated users can log in using their credentials and receive a session token.
- **Message Sending**: Users can send messages to other users within the system, stored in a MongoDB database.
- **Message Listing**: Allows users to view their past messages in a conversation.

---

## **Technologies Used**

- **Python** – Programming language used to build both the client and server.
- **Flask** – Lightweight web framework for the backend.
- **MongoDB** – NoSQL database for storing user data and messages.
- **JSON** – Used for data exchange between client and server.

---

## **Installation**

### **Prerequisites**

To run this project, you need the following installed on your system:

- Python 3.x
- MongoDB (installed and running locally or remotely)

### **Setting Up the Project**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vedang456/CORECHAT.git
   cd CORECHAT
   ```

2. **Create a virtual environment** (recommended but optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Use the `requirements.txt` to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   Ensure that MongoDB is running locally (or update the MongoDB connection string to point to your remote database). Start the server with:
   ```bash
   flask --app server run
   ```

   The server should now be running on `http://localhost:5000`.

---

## **Usage**

### **Client Interaction**

1. **Start the client** by running:
   ```bash
   python client.py
   ```

2. **Main Menu**:
   - **Option 1**: Register a new user.
   - **Option 2**: Login with an existing user.
   - **Option 3**: Exit the application.

3. **User Menu**:
   - After logging in, you can:
     - Choose another user to communicate with.
     - Send messages to the selected user.
     - View past messages with that user.
   
4. **Sending and Viewing Messages**:
   - Once in the User Menu, you can:
     - Send messages to your selected user.
     - Refresh the conversation to see the latest messages.

---

## **Endpoints (API)**

### **POST /Register**

- Registers a new user with the following fields:
  - `first_name`: User's first name
  - `last_name`: User's last name
  - `username`: Unique username
  - `password`: User's password
  - `email`: User's email address

**Response:**
- Status 201: "Added Successfully"
- Status 409: "This user already exists"

---

### **POST /Login**

- Logs in an existing user with the following fields:
  - `username`: User's username
  - `password`: User's password

**Response:**
- Status 200: Returns a session token with expiry.
- Status 404: "Wrong password" or "Invalid user."

---

### **POST /messages**

- Sends a message from the logged-in user to another user.
  - `Token`: Session token of the logged-in user.
  - `User`: The recipient's username.
  - `Message`: The content of the message.

**Response:**
- Status 201: "Message has been sent."

---

### **GET /messages**

- Retrieves messages between the logged-in user and the selected user.
  - `Token`: Session token of the logged-in user.
  - `User`: The recipient's username.

**Response:**
- Status 200: Returns a list of messages between the two users.

---

## **Future Enhancements**

- **User Authentication**: Implement password hashing and salting for better security.
- **Message Notifications**: Add real-time message notifications for users.
- **User Profiles**: Allow users to update their profile information such as display name, bio, etc.
- **Web Interface**: Develop a frontend interface for users to interact with the chat application using HTML, CSS, and JavaScript.

---

## **Contributing**

If you would like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Please ensure that your code adheres to the project's style guide and is well-documented. This project is still in progress and only v1 (non frontend application is done, also deleting message API isnt used yet)

---

## **License**

This project is open-source and available under the MIT License.

---

## **Acknowledgments**

- **Flask** for making backend development easy and efficient.
- **MongoDB** for being a flexible NoSQL database for storing data.
- **requests** for simplifying HTTP requests in Python.

---



