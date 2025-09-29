from socket import *

serverName = 'localhost'
serverPort = 45
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input command: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
numbers = input('Input numbers: ')
clientSocket.send(numbers.encode())
result = clientSocket.recv(1024)
print('From Server:', result.decode())
clientSocket.close()