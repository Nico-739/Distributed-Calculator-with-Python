import socket
import threading
from calculator import Calculator

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # This is the host
port = 8000  # Port of the host
server_socket.bind((host, port))


# Define a function to handle client connections and requests
def handle_client(client_socket, calculator):
    while True:
        # Receive client request
        request = client_socket.recv(1024).decode()
        if not request:
            break  # Client disconnected

        # Extract operation and operands from the request
        operation, operand1, operand2 = request.split(',')

        # Perform calculation using calculator instance
        try:
            if operation == 'add':
                result = calculator.add(float(operand1), float(operand2))
            elif operation == 'subtract':
                result = calculator.subtract(float(operand1), float(operand2))
            elif operation == 'multiply':
                result = calculator.multiply(float(operand1), float(operand2))
            elif operation == 'divide':
                result = calculator.divide(float(operand1), float(operand2))
            else:
                result = 'Invalid operation'
        except ValueError as e:
            result = str(e)

        # Send the result back to the client
        client_socket.send(str(result).encode())

    # Close the client socket
    client_socket.close()
    

# Calculator instance
calculator = Calculator()
