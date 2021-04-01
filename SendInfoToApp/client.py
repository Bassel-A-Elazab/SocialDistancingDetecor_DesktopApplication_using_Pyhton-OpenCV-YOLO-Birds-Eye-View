
import socket
import json

HOST = '192.168.1.4'      # The server's hostname or IP address
PORT = 7802             # The port used by the server

class ClientInfo:
    def __init__(self, time, count):
        self.time = time    
        self.count = count

    def send_information(self, time, count):
        laptop1 = ClientInfo(time, count)
        jsonStr = json.dumps(laptop1.__dict__)
        print(jsonStr)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))     
            s.sendall(bytes(jsonStr,encoding="utf-8"))
