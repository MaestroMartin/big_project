import sys
from PyQt6.QtWidgets import  QLabel, QWidget, QPushButton, QMainWindow
import requests
from PyQt6.QtCore import QTimer, QRect



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.label_c = QLabel("Temperature (C):", self)
        self.label_c.setGeometry(QRect(10, 10, 200, 30))
        
        self.label_f = QLabel("Temperature (F):", self)
        self.label_f.setGeometry(QRect(10, 50, 200, 30))
        
        self.label_time = QLabel("Time:", self)
        self.label_time.setGeometry(QRect(10, 90, 200, 30))
        
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.setGeometry(QRect(10, 130, 100, 30))
        self.refresh_button.clicked.connect(self.get_temperature)

        # Timer for automatic refresh
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_temperature)
        self.timer.start(60000)  # Refresh every 60 seconds

        self.setWindowTitle("Thermometer")
        self.setGeometry(100, 100, 300, 200)  # Set the window size and position
        self.get_temperature()

    def get_temperature(self):
        try:
            response = requests.get('http://192.168.0.116:5000/temperature')
            data = response.json()

            if 'error' in data:
                self.label_c.setText("Error: " + data['error'])
                self.label_f.setText("")
                self.label_time.setText("")
            else:
                self.label_c.setText(f"Temperature (C): {data['temp_c']}")
                self.label_f.setText(f"Temperature (F): {data['temp_f']}")
                self.label_time.setText(f"Time: {data['timestamp']}")
        except Exception as e:
            self.label_c.setText(f"Error: {str(e)}")
            self.label_f.setText("")
            self.label_time.setText("")

    

