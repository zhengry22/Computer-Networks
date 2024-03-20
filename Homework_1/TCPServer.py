from socket import *
import random

# Data of server side
serverPort = 12345

# Use TCP
serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET is the type of socket for IPv4

# As the server, we need to bind the port number on the socket
serverSocket.bind(('', serverPort))

# We welcome the TCP requests from clients, and welcome maximum 5 connections at one time
serverSocket.listen(1)

print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()
print(f"Connection Socket is: {connectionSocket}, address of client is: {addr}")

def game():
    # Generate a random int between 1 and 100 and the time we spent to guess the number
    random_int = random.randint(1, 100)
    print(random_int)
    guess_time = 0
    
    while True:
        guess = connectionSocket.recv(1024).decode()
        if not guess:
            print("Client disconnected.")
            break
        
        guess_time += 1
        # convert the guess into int
        try:
            guess_int = int(guess)
        except ValueError:
            print("Invalid input received.")
            continue
        
        print(guess)
        
        if guess_int == random_int:
            feedback = f"Congratulations! You win with {guess_time} guesses! Would you like to start a new game? [y for yes / other input for no]"
            connectionSocket.send(feedback.encode())
            resp = connectionSocket.recv(1024).decode()
            print("receiving response")
            if resp != "y":
                print("leaving!")
                connectionSocket.close()  # Close the connection socket
                return  # Exit the current game
            else:
                print("Here")
                game()
                return  # Exit the current game
        elif guess_int < random_int:
            feedback = "Smaller than answer! Try again! "
        else: 
            feedback = "Greater than answer! Try again! "
        # There might be a chance for guess to be null
        connectionSocket.send(feedback.encode())
    
    connectionSocket.close()  # Close the connection socket if client disconnected

game()
print("Game over!")
# connectionSocket.close()  # No need to close here, as it's closed inside the game function
