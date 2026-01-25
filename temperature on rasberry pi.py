from flask import Flask, jsonify
import os
import glob
import time

app = Flask(__name__)

# Load the required kernel modules for the temperature sensor
def load_modules():
    os.system('modprobe w1-gpio')  # Load the GPIO module for 1-wire communication
    os.system('modprobe w1-therm')  # Load the 1-wire temperature sensor module

# Find the folder containing the temperature sensor's data
def find_device_folder(base_dir):
    device_folders = glob.glob(base_dir + '28*')  # Search for folders with '28*' (sensor prefix)
    if device_folders:
        return device_folders[0]  # Return the first matching device folder
    else:
        raise FileNotFoundError(f"No device folders found in directory: {base_dir}")

# Read the raw temperature data from the sensor's file
def read_temp_raw(device_file):
    with open(device_file, 'r') as f:
        lines = f.readlines()  # Read all lines from the device file
    return lines

# Parse and process the temperature data to get Celsius, Fahrenheit, and timestamp
def read_temp(device_file):
    lines = read_temp_raw(device_file)
    # Loop until the sensor's output indicates a valid reading ('YES')
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')  # Find the position of the temperature data
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]  # Extract temperature value as string
        temp_c = float(temp_string) / 1000.0  # Convert raw value to Celsius
        temp_f = temp_c * 9.0 / 5.0 + 32.0  # Convert Celsius to Fahrenheit
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
        return temp_c, temp_f, timestamp

# Define a route to handle the temperature request via API
@app.route('/temperature', methods=['GET'])
def temperature():
    try:
        load_modules()  # Load the required modules
        base_dir = '/sys/bus/w1/devices/'  # Base directory for the temperature sensor
        device_folder = find_device_folder(base_dir)  # Find the sensor's device folder
        device_file = device_folder + '/w1_slave'  # The file containing the sensor data
        temp_c, temp_f, timestamp = read_temp(device_file)  # Read the temperature and timestamp
        return jsonify({"temp_c": temp_c, "temp_f": temp_f, "timestamp": timestamp})  # Return as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error if something goes wrong

# Start the Flask server and listen on all network interfaces on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
