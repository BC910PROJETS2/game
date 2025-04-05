import socket
import threading
import random

# Generate a random number for the game
target_number = random.randint(1, 100)
print(f"[INFO] The secret number is {target_number}")

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  # Host and port
server_socket.listen(5)  # Allow up to 5 simultaneous connections
print("[INFO] Server is running and waiting for connections...")

clients = []

# Broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)

# Handle each connected client
def handle_client(client_socket, address):
    print(f"[INFO] Player {address} has connected.")
    client_socket.send("Welcome to the Number Guessing Game! Guess a number between 1 and 100.".encode())
    clients.append(client_socket)

    while True:
        try:
            # Receive a guess from the client
            guess = client_socket.recv(1024).decode()
            if not guess:
                break
            try:
                guess = int(guess)
                if guess < target_number:
                    response = f"[{address}] Too low! Try again."
                elif guess > target_number:
                    response = f"[{address}] Too high! Try again."
                else:
                    response = f"[{address}] Congratulations! You guessed it!"
                    broadcast(response)
                    break
                broadcast(response)
            except ValueError:
                client_socket.send("Invalid input! Please enter a valid number.".encode())
        except:
            clients.remove(client_socket)
            break

    print(f"[INFO] Player {address} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

# Accept multiple client connections
while True:
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()

