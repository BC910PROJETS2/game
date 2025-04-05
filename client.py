import socket

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 12345)  # Server's IP and port
client_socket.connect(server_address)

print(client_socket.recv(1024).decode())  # Receive welcome message from server

while True:
    guess = input("Enter your guess: ")  # Player enters a guess
    client_socket.send(guess.encode())  # Send the guess to the server
    response = client_socket.recv(1024).decode()  # Receive feedback from the server
    print(response)
    if "Congratulations" in response:
        break  # Game ends when the player guesses correctly

client_socket.close()
