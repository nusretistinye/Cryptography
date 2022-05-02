from Des import *
import socket

server = socket.socket()
host = socket.gethostname()
ip_Address = socket.gethostbyname(host)
portNumber = 8080
 
host = ip_Address
username = "Bob" #input('')

server.connect((host, portNumber))
 
server.send(username.encode())
server_name = server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' joined')

while True:
    key = "secretkeyOfNusretAraz"
    k = des(key)

    message = server.recv(1024)
    print(server_name, ":", message)
    print("Decrypted Message:", k.decrypt(message))
    message = input("message to send : ")
    
    Input_encrypted = k.encrypt(message)
    print("Encrypted Message:")
    print(Input_encrypted)
    server.send(Input_encrypted)  