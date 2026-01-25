import json
import hashlib
import os

# Registration class to handle user registration, password hashing, and JSON file management
class Registration:
    def __init__(self, username, password, data):
        super().__init__()
        self.username = username
        self.password = password
        self.data = self.load()  # Load existing users from JSON file

    # Load user data from the JSON file, handle missing file or decoding errors
    def load(self):
        try:
            with open("ID_big_project.json", "r") as file:
                data = json.load(file)  # Load the JSON data
                return data["USERS"]  # Return the list of users
        except FileNotFoundError:
            print("JSON file not found.")  # Handle missing JSON file
            return []
        except json.JSONDecodeError:
            print("Error decoding Json.")  # Handle JSON decoding errors
            return []

    # Save the user data back to the JSON file
    def save(self):
        with open("ID_big_project.json", "w") as file:
            json.dump({"USERS": self.data}, file, indent=2)  # Write users back to the file

    # Validate the length of the username
    def first_part(self, entered_username):
        if len(entered_username) <= 6:
            print("You have a short username!")  # Ensure username is longer than 6 characters
            return entered_username

    # Validate the length of the password
    def second_part(self, entered_password, entered_again_password):
        if len(entered_password) <= 6 and len(entered_again_password) <= 6:
            print("You have a short password!")  # Ensure password is longer than 6 characters
            return False
        return True

    # Verify if the username is already in use and check if the passwords match
    def verify(self):
        for user in self.data:
            if user["username"] == self.username:
                print("This username is already used")  # Check for duplicate username
                return False
        if self.password != entered_password:
            print("Incorrect password")  # Check if the passwords match
            return False
        print("You are successfully logged in")  # Successful login
        return True

    # Create a new account with hashed password and salt
    def creating_new_acc(self, entered_again_password):
        salt = self.generate_salt()  # Generate a unique salt for password hashing
        password_hash = self.hash_password(entered_again_password, salt)  # Hash the password
        self.data.append({
            "username": self.username,
            "password_hash": password_hash,  # Store the hashed password
            "salt": salt.hex()  # Store the salt as a hexadecimal string
        })
        self.save()  # Save the new account to the JSON file

    # Generate a random salt for password hashing
    def generate_salt(self, length=16):
        return os.urandom(length)

    # Hash the password with salt using SHA-256
    def hash_password(self, password, salt):
        return hashlib.sha256(password.encode() + salt).hexdigest()

# Get the username and password from the user
entered_username = input("Write your username: ")
entered_password = input("Write your password: ")
entered_again_password = input("Write your password again: ")

# Create an instance of the Registration class
reg = Registration(entered_username, entered_password, [])

# Check the length of the passwords
if not reg.second_part(entered_password, entered_again_password):
    print("Registration failed. Please enter a valid password.")
else:
    # Create a new account
    reg.creating_new_acc(entered_again_password)
    print("Registration successful!")
