import socket
import time
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCCONNECT_MESSAGE = "DISCONNECTED"
SERVER ="10.201.98.100" 
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" "*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2040).decode(FORMAT))

send("Hello wolrd!!!!!")
time.sleep(1)

send("Hello Everyone!!!!!")
time.sleep(1)

send("Hello mam!!!!!")
time.sleep(1)

send("Hello worl!!!!!")

send(DISCCONNECT_MESSAGE)