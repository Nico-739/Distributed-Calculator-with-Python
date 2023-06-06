import socket
import threading
from datetime import datetime

# Create a Logger socket
logger_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all network interfaces
port = 9000  # Port number for Logger

# Bind the socket to the host and port
logger_socket.bind((host, port))

# Function to log the request and result
def log_request_result(request, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Request: {request}, Result: {result}\n"
    with open("calculator_logs.txt", "a") as file:
        file.write(log_entry)
    print(f"Logged request and result: {request}, {result}")

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Logger: Connected to Spooler: {address}")

    # Receive the request from the client
    request = client_socket.recv(1024).decode()
    print(f"Logger: Received request: {request}")

    # Receive the result from the client
    result = client_socket.recv(1024).decode()
    print(f"Logger: Received result: {result}")

    # Log the request and result
    log_request_result(request, result)

    # Close the client socket
    client_socket.close()
    print(f"Logger: Disconnected from Spooler: {address}")

# Start listening for connections from the Spooler
logger_socket.listen()

print("Logger is running and listening for connections...")

while True:
    # Accept a client connection
    client_socket, address = logger_socket.accept()

    # Handle the client request in a separate thread
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
