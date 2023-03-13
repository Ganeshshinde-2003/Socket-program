import socket
import threading

HEADER = 64
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCCONNECT_MESSAGE = "DISCONNECTED"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client (conn, addr):
    print(f"[new conncetion] {addr} connected\n")
    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)

            if msg == DISCCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("MSG received".encode(FORMAT))
    conn.close()
        
def start():
    server.listen()
    print(f"[LISTENING] server is listenig on {server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[active connection] {threading.active_count() -1}")

print("[starting] server is starting...")
start()
