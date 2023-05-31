import socket
import threading
from calculator import Calculator

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # This is the host
port = 8000  # Port of the host
server_socket.bind((host, port))
