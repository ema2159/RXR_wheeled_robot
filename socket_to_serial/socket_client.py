import socket
import time
import random

HOST = '10.138.226.50'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = str.encode(str(random.randint(0, 100))+","+str(random.randint(0, 100)))
        s.send(data)
        time.sleep(0.1)
        
