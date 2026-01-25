import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt6.QtGui import QPalette, QColor
from userlook import MainWindow  # Import the main application window from another file

# Widget to handle setting a background color
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paletta = self.palette()
        paletta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paletta)

# Login window class to handle user login
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle("Martin_first")
        self.setToolTip("Cursor")  # Tooltip for the window
        self.initUI()

    # Initialize UI components (labels, text fields, buttons)
    def initUI(self):
        self.entered_username_label = QLabel(self)
        self.entered_username_label.setText("Enter your username: ")
        self.entered_username_label.move(50, 50)

        self.txt_entered_username = QLineEdit(self)
        self.txt_entered_username.move(200, 50)
        self.txt_entered_username.resize(250, 32)

        self.entered_password_label = QLabel(self)
        self.entered_password_label.setText("Enter your password:")
        self.entered_password_label.move(50, 90)

        self.txt_entered_password = QLineEdit(self)
        self.txt_entered_password.move(200, 90)
        self.txt_entered_password.resize(250, 32)
        self.txt_entered_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.move(200, 130)
        self.btn_login.clicked.connect(self.handle_login)

        self.register_button = QPushButton("Register", self)
        self.register_button.move(250, 170)
        self.register_button.clicked.connect(self.open_registration)

    # Handle login logic
    def handle_login(self):
        from log_in import User  # Import user authentication class
        entered_username = self.txt_entered_username.text()
        entered_password = self.txt_entered_password.text()
        user = User(entered_username, entered_password)
        if user.login(entered_username, entered_password):  # Verify username and password
            QMessageBox.information(self, "Success", "Login successful")
            self.open_main_window()  # Open main application window upon successful login
        else:
            QMessageBox.warning(self, "Failed", "Login failed")

    # Open the registration window if the user wants to register
    def open_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()
        self.close()

    # Open the main window of the application
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

# Registration window class to handle new user registrations
class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle("Martin_first")
        self.setToolTip("Cursor")
        self.initUI()

    # Initialize the UI for the registration window
    def initUI(self):
        self.entered_username_label = QLabel(self)
        self.entered_username_label.setText("Enter your username: ")
        self.entered_username_label.move(50, 50)
        self.entered_username_label.resize(150, 32)

        self.txt_entered_username = QLineEdit(self)
        self.txt_entered_username.move(250, 50)
        self.txt_entered_username.resize(250, 32)

        self.entered_password_label = QLabel(self)
        self.entered_password_label.setText("Enter your password: ")
        self.entered_password_label.move(50, 90)
        self.entered_password_label.resize(150, 32)

        self.txt_entered_password = QLineEdit(self)
        self.txt_entered_password.move(250, 90)
        self.txt_entered_password.resize(250, 32)
        self.txt_entered_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.entered_again_password_label = QLabel(self)
        self.entered_again_password_label.setText("Enter your password again: ")
        self.entered_again_password_label.move(50, 130)
        self.entered_again_password_label.resize(150, 32)
        
        self.txt_entered_again_password = QLineEdit(self)
        self.txt_entered_again_password.move(250, 130)
        self.txt_entered_again_password.resize(250, 32)
        self.txt_entered_again_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_register = QPushButton("Register", self)
        self.btn_register.move(250, 170)
        self.btn_register.clicked.connect(self.handle_registration)

        self.login_button = QPushButton("Back to Login", self)
        self.login_button.move(250, 210)
        self.login_button.clicked.connect(self.open_login_window)

    # Handle the registration logic
    def handle_registration(self):
        from registration import Registration  # Import registration class

        entered_username = self.txt_entered_username.text()
        entered_password = self.txt_entered_password.text()
        entered_again_password = self.txt_entered_again_password.text()
        reg = Registration(entered_username, entered_password, [])

        # Check if both passwords match and register the user
        if entered_password == entered_again_password:
            QMessageBox.information(self, "Success", "Registration successful")
            self.open_login_window()  # Return to login after successful registration
        elif not reg.second_part(entered_password, entered_again_password):  # Password validation
            print("Registration failed. Please enter a valid password.")
        elif reg.creating_new_acc(entered_again_password):  # Create new account
            print("Registration successful!")
        else:
            QMessageBox.warning(self, "Failed", "Passwords do not match")

            if reg.creating_new_acc(entered_again_password):  # If account creation succeeds
                QMessageBox.information(self, "Success", "Registration successful")
                self.open_login_window()  # Return to login window
            else:
                QMessageBox.warning(self, "Failed", "Registration failed")

    # Return to the login window
    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

# Start the application window
def window():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()
