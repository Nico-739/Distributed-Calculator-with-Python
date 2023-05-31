import tkinter as tk
import socket

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'netnode_ip_address'  # Replace with the actual IP address of the NetNode
port = 8000  # Port number used by the NetNode

# Connect to the NetNode
client_socket.connect((host, port))

# Function to send a request to the NetNode and receive the result
def send_request():
    operation = operation_variable.get()
    operand1 = operand1_entry.get()
    operand2 = operand2_entry.get()
    request = f"{operation},{operand1},{operand2}"
    client_socket.send(request.encode())
    result = client_socket.recv(1024).decode()
    result_label.config(text=f"Result: {result}")

# Function to handle client disconnection
def disconnect():
    client_socket.close()
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("Distributed Calculator")
window.geometry("400x300")
window.configure(bg="white")

# Create GUI elements
operation_label = tk.Label(window, text="Operation:", font=("Arial", 14), bg="white")
operation_variable = tk.StringVar()
operation_dropdown = tk.OptionMenu(window, operation_variable, "add", "subtract", "multiply", "divide")
operand1_label = tk.Label(window, text="Operand 1:", font=("Arial", 14), bg="white")
operand1_entry = tk.Entry(window, font=("Arial", 14))
operand2_label = tk.Label(window, text="Operand 2:", font=("Arial", 14), bg="white")
operand2_entry = tk.Entry(window, font=("Arial", 14))
calculate_button = tk.Button(window, text="Calculate", command=send_request, font=("Arial", 14), bg="#4CAF50", fg="white")
result_label = tk.Label(window, text="Result:", font=("Arial", 14), pady=10, bg="white")
disconnect_button = tk.Button(window, text="Disconnect", command=disconnect, font=("Arial", 14), bg="#f44336", fg="white")

# Arrange GUI elements using grid layout
operation_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
operation_dropdown.grid(row=0, column=1, pady=10)
operand1_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
operand1_entry.grid(row=1, column=1, pady=10)
operand2_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
operand2_entry.grid(row=2, column=1, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2)
disconnect_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Configure grid weights to make elements expandable
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure((0, 1), weight=1)

# Start the GUI event loop
window.mainloop()

# Close the client socket
client_socket.close()
