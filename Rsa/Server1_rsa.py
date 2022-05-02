import socket
from rsa import *

server = socket.socket()
host = socket.gethostname()
ip_Address = socket.gethostbyname(host)
portNumber = 8080
 
server.bind((host, portNumber))
print("Binded:", ip_Address)
 
name = 'Alice' #input('')

#Generate RSA keys
GenerateKeys(name)

server.listen(1) 
conn, add = server.accept()
print(add[0], " Connected")
client = (conn.recv(1024)).decode()
conn.send(name.encode())

while True:
    message = input('message to send : ')
    print("Encrypting using the public Key of ", client)
    Encrypted_Message = encrypt(message, client +'_public.txt')
    #print(decrypt("Alice",Input_encrypted))

    #decrypted = decrypt(client,Input_encrypted)
    #print(decrypted)
    print("Encrypted Message:")
    print(Encrypted_Message)
    conn.send(Encrypted_Message.encode())

    #Reveive part
    message = conn.recv(1024)
    message = message.decode("UTF-8")
    print(client, ":", message)
    print("Decrypt using the Private Key of ", name)
    print(name, ":", decrypt(name,message))