import socket
import random

# Create a Spooler socket
spooler_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all network interfaces
port = 7000  # Port number for Spooler

# Bind the socket to the host and port
spooler_socket.bind((host, port))

# List of available Calculators
calculator_addresses = [('calculator1_ip', 9001), ('calculator2_ip', 9002)]

# Function to distribute requests to Calculators
def distribute_request(request):
    # Randomly select a Calculator from the list
    calculator_address = random.choice(calculator_addresses)

    # Create a socket to connect to the selected Calculator
    calculator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    calculator_socket.connect(calculator_address)

    # Send the request to the Calculator
    calculator_socket.send(request.encode())

    # Receive the result from the Calculator
    result = calculator_socket.recv(1024).decode()

    # Close the connection to the Calculator
    calculator_socket.close()

    return result

# Start listening for connections from the Client
spooler_socket.listen()

print("Spooler is running and listening for connections...")

while True:
    # Accept a connection from the Client
    client_socket, address = spooler_socket.accept()

    # Receive the request from the Client
    request = client_socket.recv(1024).decode()

    # Distribute the request to a Calculator and get the result
    result = distribute_request(request)

    # Send the result back to the Client
    client_socket.send(result.encode())

    # Close the connection to the Client
    client_socket.close()
