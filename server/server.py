import socket
from _thread import start_new_thread
import sys

SERVER = '192.168.1.104'
PORT = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str (e)

s.listen(10)
print("waiting for a connection, server Started")


def threaded_client(conn):
    
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # if get error incress the data
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnect")
                break
            else:
                print(f"Received: {reply}")
                print(f"Sending: {reply}")

            conn.sendall(str.encode(reply))
        except:
            break
    print("Connection Closed")
    conn.close()
    
while True:
    conn, addr = s.accept()
    print(f"Connected to {addr}")

    start_new_thread(threaded_client, (conn,))