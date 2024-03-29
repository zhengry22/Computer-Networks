from socket import *

# Data of server side
# Input serverName
# serverName ='127.0.0.1' # LocalHost
serverName = input("Please input IP Address\n")
serverPort = 12345

# Use TCP
clientSocket = socket(AF_INET, SOCK_STREAM) # AF_INET is the type of socket for IPv4

# Connect to server
clientSocket.connect((serverName, serverPort))
print('Welcome to the guessing game! ')

while True:
    guess = input('Please enter your guess\n')
    if not guess:
        print("Can't send empty message! ")
    else:     
        try:
            guess_int = int(guess)
            clientSocket.send(guess.encode()) # To send the msg in TCP, we don't need to implicitly provide the destination, 
            # since the connection is already formed 
            feedback = clientSocket.recv(1024)
            server_msg = feedback.decode()
            print(f"From server: {server_msg}")
            if server_msg.startswith("Congratulations"):
                # Time to make a decision!
                choice = input()
                clientSocket.send(choice.encode())
                if (choice != "y"):
                    break
        except Exception as e:
            print(e)
            print("Your input must be a valid number")   

clientSocket.close()