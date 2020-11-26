import time
import serial
import random

ser = serial.Serial(
    port="/dev/ttyUSB0",  # Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    baudrate=115200,
    timeout=1,
)

while 1:
    data = (
        str(random.randint(0, 100))
        + ","
        + str(random.randint(0, 100))
        + ","
        + str(random.randint(0, 100))
        + "\n"
    )
    ser.write(data.encode())
    time.sleep(0.6)
