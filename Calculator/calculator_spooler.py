import socket
import random

# Create a Spooler socket
spooler_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all network interfaces
port = 7000  # Port number for Spooler

# Bind the socket to the host and port
spooler_socket.bind((host, port))

# List of available Calculators
calculator_addresses = [('127.0.0.1', 9001), ('127.0.0.1', 9002)]

# Function to distribute requests to Calculators
def distribute_request(request):
    # Randomly select a Calculator from the list
    calculator_address = random.choice(calculator_addresses)

    # Create a socket to connect to the selected Calculator
    calculator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    calculator_socket.connect(calculator_address)

    # Send the request to the Calculator
    calculator_socket.send(request.encode())
    print(f"Sent request to Calculator: {calculator_address}")

    # Receive the result from the Calculator
    result = calculator_socket.recv(1024).decode()
    print(f"Received result from Calculator: {calculator_address}")

    # Close the connection to the Calculator
    calculator_socket.close()

    return result

# Start listening for connections from the Client and Calculators
spooler_socket.listen()

print("Spooler is running and listening for connections...")

while True:
    # Accept a connection
    client_socket, address = spooler_socket.accept()
    print(f"Connected to client: {address}")

    # Receive the request
    request = client_socket.recv(1024).decode()
    print(f"Received request: {request}")

    # Distribute the request to a Calculator and get the result
    result = distribute_request(request)
    print(f"Distributed request to Calculators")

    # Send the result back to the Client
    client_socket.send(result.encode())
    print(f"Sent result to client")

    # Close the connection
    client_socket.close()
    print(f"Disconnected from client: {address}")
