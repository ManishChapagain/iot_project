import serial
import time

device = 'COM5'

try:
    print("Trying... "+ device)
    arduino = serial.Serial(device, 9600)
except:
    print("Error occured while connecting to "+ device)

while True:
    time.sleep(1)
    try:
        data = arduino.readline()
        print(data.strip().decode("utf-8"))
    except:
        print('Processing')
