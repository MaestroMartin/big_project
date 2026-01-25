import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt6.QtGui import QPalette, QColor, QPixmap, QPalette
from PyQt6.QtCore import Qt





class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Martin_first")
        self.setToolTip("Cursor")
        self.initUI()
        
    def initUI(self):
        self.screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (self.screen_geometry.width() - 700) // 2
        y = (self.screen_geometry.height() - 700) // 2
        self.setGeometry(x, y, 700, 700)
        
        # Username field
        self.entered_username_label = QLabel(self)
        self.entered_username_label.setText("Enter your username: ")
        self.entered_username_label.move(50, 50)

        self.txt_entered_username = QLineEdit(self)
        self.txt_entered_username.move(200, 50)
        self.txt_entered_username.resize(250, 32)

        # Password field
        self.entered_password_label = QLabel(self)
        self.entered_password_label.setText("Enter your password:")
        self.entered_password_label.move(50, 90)

        self.txt_entered_password = QLineEdit(self)
        self.txt_entered_password.move(200, 90)
        self.txt_entered_password.resize(250, 32)
        self.txt_entered_password.setEchoMode(QLineEdit.EchoMode.Password)

        # Buttons
        self.btn_login = QPushButton("Login", self)
        self.btn_login.move(200, 130)
        self.btn_login.clicked.connect(self.handle_login)

        self.register_button = QPushButton("Register", self)
        self.register_button.move(250, 170)
        self.register_button.clicked.connect(self.open_registration)

    def handle_login(self):
        from log_in import User
        entered_username = self.txt_entered_username.text()
        entered_password = self.txt_entered_password.text()
        user = User(entered_username, entered_password)
        
        if user.login(entered_username, entered_password):  # Verification of username and password
            QMessageBox.information(self, "Success", "Login successful")
            self.open_main_window()  # Open the main window
        else:
            QMessageBox.warning(self, "Failed", "Login failed")

    def open_registration(self):
        print("Opening registration window...")
        try:
            from registration_window import RegistrationWindow  # Import RegistrationWindow třídy
            self.hide()  # Skrytí přihlašovacího okna
            self.registration_window = RegistrationWindow()  # Vytvoření instance
            self.registration_window.show()  # Zobrazení registračního okna
        except Exception as e:
            print(f"Error opening registration window: {str(e)}")
            QMessageBox.warning(self, "Error", f"Failed to open registration window: {str(e)}")

    def open_main_window(self):
        from userlook import MainWindow  # Import MainWindow třídy z userlook.py
        print("Opening main window...")
        self.main_window = MainWindow()  # Předpokládám, že MainWindow je třída definovaná v userlook
        self.main_window.show()
        self.close()  # Zavření přihlašovacího okna po úspěšném přihlášení
    


def window():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
