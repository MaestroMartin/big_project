import json
import os
import hashlib

# User class to handle user login, password hashing, and loading user data from JSON
class User:
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.data = self.load()  # Load the existing users from the JSON file

    # Load user data from the JSON file
    def load(self):
        try:
            with open("ID_big_project.json", "r") as file:
                data = json.load(file)  # Load the JSON data
                return data["USERS"]  # Return the list of users
        except FileNotFoundError:
            print("JSON file not found.")  # Handle missing file
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON.")  # Handle JSON decoding errors
            return []

    # Validate username length
    def first_part(self, entered_username):
        if len(entered_username) <= 6:
            print("You have a short username!")  # Ensure the username is longer than 6 characters
            return entered_username

    # Validate password length
    def second_part(self, entered_password, entered_username):
        if len(entered_password) <= 8:
            print("You have a short password!")  # Ensure the password is longer than 8 characters
            return entered_username

    # Generate a random salt for password hashing
    def generate_salt(self, length=16):
        return os.urandom(length)

    # Hash the password with salt using SHA-256
    def hash_password(self, password, salt):
        return hashlib.sha256(password.encode() + salt).hexdigest()

    # Login function to verify the username and password
    def login(self, entered_username, entered_password):
        for user in self.data:
            if user['entered_username'] == entered_username:  # Check if the username exists
                salt = bytes.fromhex(user['salt'])  # Retrieve the stored salt
                entered_password_hash = self.hash_password(entered_password, salt)  # Hash the entered password
                if user['password_hash'] == entered_password_hash:  # Check if the password hash matches
                    print("You are successfully logged in")
                    return True
                else:
                    print("Incorrect password")
                    return False
        print("Incorrect username")
        return False

# Get the username and password from the user
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Create an instance of the User class and attempt login
user = User(entered_username, entered_password)
user.login(entered_username, entered_password)
