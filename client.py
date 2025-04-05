import socket

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))  # Server IP and port

print(client_socket.recv(1024).decode())  # Welcome message

while True:
    guess = input("Enter your guess: ")  # Player enters a guess
    client_socket.send(guess.encode())  # Send guess to the server
    response = client_socket.recv(1024).decode()  # Receive server response
    print(response)
    if "Congratulations" in response:
        break

client_socket.close()
