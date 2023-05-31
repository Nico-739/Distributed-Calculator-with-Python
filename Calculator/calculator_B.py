import socket

# Create a Calculator socket
calculator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all network interfaces
port = 9002  # Port number for Calculator B

# Bind the socket to the host and port
calculator_socket.bind((host, port))

# Function to perform the requested calculation
def perform_calculation(request):
    operation, operand1, operand2 = request.split(',')
    result = None

    if operation == 'add':
        result = str(float(operand1) + float(operand2))
    elif operation == 'subtract':
        result = str(float(operand1) - float(operand2))
    elif operation == 'multiply':
        result = str(float(operand1) * float(operand2))
    elif operation == 'divide':
        result = str(float(operand1) / float(operand2))

    return result

# Start listening for connections from the Spooler
calculator_socket.listen()

print("Calculator B is running and listening for connections...")

while True:
    # Accept a connection from the Spooler
    spooler_socket, address = calculator_socket.accept()
    print(f"Connected to Spooler: {address}")

    # Receive the request from the Spooler
    request = spooler_socket.recv(1024).decode()
    print(f"Received request: {request}")

    # Perform the calculation
    result = perform_calculation(request)

    # Send the result back to the Spooler
    spooler_socket.send(result.encode())
    print(f"Sent result: {result}")

    # Close the connection to the Spooler
    spooler_socket.close()
