import socket

# Create a Calculator socket
calculator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all network interfaces
port = 9001  # Port number for Calculator

# Bind the socket to the host and port
calculator_socket.bind((host, port))

# Function to perform the requested calculation
def perform_calculation(request):
    operation, operand1, operand2 = request.split(',')
    result = None

    if operation == 'add':
        result = float(operand1) + float(operand2)
    elif operation == 'subtract':
        result = float(operand1) - float(operand2)
    elif operation == 'multiply':
        result = float(operand1) * float(operand2)
    elif operation == 'divide':
        result = float(operand1) / float(operand2)

    return str(result)

# Start listening for connections from the NetNode
calculator_socket.listen()

print("Calculator is running and listening for connections...")

while True:
    # Accept a connection from the NetNode
    netnode_socket, address = calculator_socket.accept()

    # Receive the request from the NetNode
    request = netnode_socket.recv(1024).decode()

    # Perform the calculation
    result = perform_calculation(request)

    # Send the result back to the NetNode
    netnode_socket.send(result.encode())

    # Close the connection to the NetNode
    netnode_socket.close()
