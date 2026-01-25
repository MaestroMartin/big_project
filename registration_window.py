
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel



class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Window")
        self.setToolTip("Registration Window")
        self.initUI()

    def initUI(self):
        self.screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (self.screen_geometry.width() - 700) // 2
        y = (self.screen_geometry.height() - 700) // 2  
        self.setGeometry(x, y, 700, 700)

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


    def handle_registration(self):
        from registration import Registration  # Import dovnitř metody

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
        
    
    def open_login_window(self):
        from login_start_window import LoginWindow
        self.login_start_window = LoginWindow()
        self.hide()  # Skrytí registračního okna
        self.login_start_window.show()  # Zobrazení přihlašovacího okna (rodičovské okno)

