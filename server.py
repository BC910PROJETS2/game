import socket
import threading
import random

# Generate the random number
target_number = random.randint(1, 100)
print(f"[INFO] Secret number generated: {target_number}")

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  # Host and port
server_socket.listen(5)
print("[INFO] Server is running and waiting for players...")

# Handle each player's connection
def handle_player(conn, addr):
    print(f"[INFO] Player {addr} has connected.")
    conn.send("Welcome to the Number Guessing Game! Guess a number between 1 and 100.".encode())
    
    while True:
        try:
            guess = conn.recv(1024).decode()  # Receive guess from player
            if not guess:
                break
            guess = int(guess)
            if guess < target_number:
                conn.send("Too low! Try again.".encode())
            elif guess > target_number:
                conn.send("Too high! Try again.".encode())
            else:
                conn.send("Congratulations! You guessed the number!".encode())
                print(f"[INFO] Player {addr} guessed the number! The game is over.")
                conn.close()
                break
        except ValueError:
            conn.send("Invalid input! Please enter a number.".encode())
    
    print(f"[INFO] Player {addr} disconnected.")

# Accept multiple players
while True:
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_player, args=(conn, addr)).start()
