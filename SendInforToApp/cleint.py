
import socket, pickle
import json
import base64 , urllib
from json import JSONEncoder
import numpy as np 


HOST = '10.2.0.16'      # The server's hostname or IP address
PORT = 7802             # The port used by the server

class Laptop:
    def __init__(self, time, count):
        self.time = time    
        self.count = count

laptop1 = Laptop('18.20', '10')
jsonStr = json.dumps(laptop1.__dict__)
print(jsonStr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))     
    s.sendall(bytes(jsonStr,encoding="utf-8"))
