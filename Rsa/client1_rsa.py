import socket
from rsa import *

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
 
print('This is your IP address: ',ip)
server_host = ip #input('')
name = "Bob" #input('')

#Crate RSA keys for Bob
GenerateKeys(name)
 
socket_server.connect((server_host, sport))
 
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' has joined...')
while True:
    received_message = socket_server.recv(1024)
    message = received_message.decode("UTF-8")
    print(server_name, ":", message)
    print(server_name, ":", decrypt(name,message))

    message = input("message to send : ")
    
    print("Encrypting using the Public Key of ", server_name)
    Input_encrypted = encrypt(message, server_name + '_public.txt')
    print("Encrypted Text:")
    print(Input_encrypted)
    socket_server.send(Input_encrypted.encode())  