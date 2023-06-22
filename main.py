import serial
import pandas as pd
from datetime import datetime
import time

# Serial port settings
serial_port = 'COM3'  # Replace with your serial port
baud_rate = 9600

# Duration of data collection (in seconds)
collection_duration = 1000  # Replace with your desired duration

# Initialize serial connection
ser = serial.Serial(serial_port, baud_rate)

# Create a list to store the data
data = []

# Start time of data collection
start_time = time.time()

# Read data from serial port for the specified duration
while (time.time() - start_time) < collection_duration:
    line = ser.readline().decode('utf-8').strip()

    # Parse the received line as a JSON string
    if line.startswith("{'co2ppm':") and line.endswith("}"):
        try:
            co2_value = int(line.split(':')[1].split('}')[0])
            timestamp = datetime.now()

            # Add data to the list
            data.append([timestamp, co2_value])

            print(f"Timestamp: {timestamp}, CO2 ppm: {co2_value}")
        except ValueError:
            print("Error parsing CO2 value")

# Close the serial connection
ser.close()

# Save data to a CSV file
date_string = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
csv_filename = f"{date_string}_sensordata.csv"
df = pd.DataFrame(data, columns=['Timestamp', 'CO2 ppm'])
print(df)
df.to_csv(f'data\\{date_string}_data.csv', index=False, decimal=',', sep=';')


print(f"Data saved to {csv_filename}")
