from socket import *
import threading
import random
import json

def service (connectionSocket):
    while True:
        data = connectionSocket.recv(1024).decode().strip()
        if not data:
            break
        try:
            req = json.loads(data)
        except Exception:
            connectionSocket.send(json.dumps({"error": "Invalid JSON"}).encode())
            break
     

        command = req.get("command")
        tal1 = req.get("tal1")
        tal2 = req.get("tal2")
    
        if command == "Done":
           break 

        command = command.lower().capitalize()  
        if command == "Random":
                response = random.randint(int(tal1), int(tal2))
        elif command == "Add":
                response = int(tal1) + int(tal2)
        elif command == "Subtract":
                response = int(tal1) - int(tal2)
        else:
                response = f"Error: Unknown command: {command}"

    
        connectionSocket.send(json.dumps({"response":response}).encode())
    connectionSocket.close()


#{"command": "Add", "tal1": 3, "tal2": 8}
#{"command": "Subtract", "tal1": 3, "tal2": 8}

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