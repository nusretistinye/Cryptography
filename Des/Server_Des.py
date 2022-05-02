from Des import *
import socket

server = socket.socket()
host = socket.gethostname()
ip_Address = socket.gethostbyname(host) 
portNumber = 8080
 
server.bind((host, portNumber))
print("Binded:", ip_Address)
 
username = 'Alice' #input('')

server.listen(1) 
conn, add = server.accept()
print(add[0], " Connected")
client = (conn.recv(1024)).decode()
print(client + ' connected') 
conn.send(username.encode())

while True:
    message = input('message to send : ')

    key = "secretkeyOfNusretAraz"
    k = des(key)
    Encrypted_Message = k.encrypt(message)

    print("Encrypted Message:")
    print(Encrypted_Message)
    #Encrypted_Message = Encrypted_Message
    #print("Decrypted Message:", k.decrypt(Encrypted_Message))

    conn.send(Encrypted_Message)

    message = conn.recv(1024)
    print(client, ":", message)
    decryptedMessage = str(k.decrypt(message))
    print(username, ":", decryptedMessage)
