from socket import *
import threading
import random

def service (connectionSocket):
    while True:
     command=connectionSocket.recv(1024).decode().strip()
     if command=='Done':
         break
     connectionSocket.send("Input numbers".encode())
     numbers=connectionSocket.recv(1024).decode().strip()

     numberarray = numbers.split(" ", 1)
     command = command.lower().capitalize()  
     if command == "Random":
                response = str(random.randint(int(numberarray[0]), int(numberarray[1])))
     elif command == "Add":
                response = str(int(numberarray[0]) + int(numberarray[1]))
     elif command == "Subtract":
                response = str(int(numberarray[0]) - int(numberarray[1]))
     else:
                response = f"Error: Unknown command: {command}"

    
     connectionSocket.send(response.encode())
    connectionSocket.close()


#serverName = 'servername'
serverPort = 45
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 45))
serverSocket.listen(3)

print('Ready to recieve')
while True:
   connectionSocket,adr = serverSocket.accept()
   '''service(connectionSocket)'''
   
   threading.Thread(target=service, args=(connectionSocket,)).start()