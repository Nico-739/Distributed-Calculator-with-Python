import socket
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

# Start listening for connections from the Spooler
logger_socket.listen()

print("Logger is running and listening for connections...")

while True:
    # Accept a connection from the Spooler
    spooler_socket, address = logger_socket.accept()
    print(f"Connected to Spooler: {address}")

    # Receive the request from the Spooler
    request = spooler_socket.recv(1024).decode()
    print(f"Received request: {request}")

    # Receive the result from the Spooler
    result = spooler_socket.recv(1024).decode()
    print(f"Received result: {result}")

    # Log the request and result
    log_request_result(request, result)

    # Close the connection to the Spooler
    spooler_socket.close()
