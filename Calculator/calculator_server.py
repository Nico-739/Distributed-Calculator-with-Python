import socket
import threading

# Create a NetNode socket
netnode_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all network interfaces
port = 8000  # Port number for NetNode

# Bind the socket to the host and port
netnode_socket.bind((host, port))

# Define the list of calculator addresses
spooler_addresses = [
    ('127.0.0.1', 7000)
]

# Function to handle client requests
def handle_client(client_socket, address):
    print(f"Server: Connected to client: {address}")

    # Receive the request from the client
    request = client_socket.recv(1024).decode()
    print("Server: Received request:", request)  # Debugging statement
    operation, operand1, operand2 = request.split(',')

    # Distribute the request to the calculators
    for calc_address in spooler_addresses:
        calc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        calc_socket.connect(calc_address)
        calc_socket.send(request.encode())
        calc_socket.close()

    # Receive the results from the calculators
    results = []
    for calc_address in spooler_addresses:
        calc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        calc_socket.connect(calc_address)
        result = calc_socket.recv(1024).decode()
        results.append(result)
        calc_socket.close()

    # Send the aggregated results back to the client
    response = ','.join(results)
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()
    print(f"Server: Disconnected from client: {address}")

# Start listening for client connections
netnode_socket.listen()

print("Server: Is running and listening for client connections...")

while True:
    # Accept a client connection
    client_socket, address = netnode_socket.accept()

    # Handle the client request in a separate thread
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
