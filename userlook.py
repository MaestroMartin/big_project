import sys
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QMainWindow
import requests
from PyQt6.QtCore import QTimer, QRect

# Main application window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()  # Initialize the user interface
    
    def initUI(self):
        # Create and position label to display temperature in Celsius
        self.label_c = QLabel("Temperature (C):", self)
        self.label_c.setGeometry(QRect(10, 10, 200, 30))
        
        # Create and position label to display temperature in Fahrenheit
        self.label_f = QLabel("Temperature (F):", self)
        self.label_f.setGeometry(QRect(10, 50, 200, 30))
        
        # Create and position label to display the last update time
        self.label_time = QLabel("Time:", self)
        self.label_time.setGeometry(QRect(10, 90, 200, 30))
        
        # Create and position a refresh button to manually update temperature
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.setGeometry(QRect(10, 130, 100, 30))
        self.refresh_button.clicked.connect(self.get_temperature)  # Connect the button to get_temperature function

        # Timer for automatic refresh every 60 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_temperature)
        self.timer.start(60000)  # Refresh every 60 seconds

        # Set window properties
        self.setWindowTitle("Thermometer")
        self.setGeometry(100, 100, 300, 200)  # Set window size and position
        self.get_temperature()  # Fetch temperature immediately when the app starts

    # Function to retrieve temperature data from an API endpoint
    def get_temperature(self):
        try:
<<<<<<< HEAD
            response = requests.get('http://192.168.0.116:5000/temperature')
=======
            response = requests.get('http://192.168.0.106:5000/temperature')  # API call to get temperature data
>>>>>>> 90057adde42a9b8f30edb306b2bf531a08854049
            data = response.json()

            # Check for any errors in the data received from the API
            if 'error' in data:
                self.label_c.setText("Error: " + data['error'])
                self.label_f.setText("")
                self.label_time.setText("")
            else:
                # Update labels with the temperature and timestamp from the API
                self.label_c.setText(f"Temperature (C): {data['temp_c']}")
                self.label_f.setText(f"Temperature (F): {data['temp_f']}")
                self.label_time.setText(f"Time: {data['timestamp']}")
        except Exception as e:
            # Display error message if something goes wrong during the API call
            self.label_c.setText(f"Error: {str(e)}")
            self.label_f.setText("")
            self.label_time.setText("")
