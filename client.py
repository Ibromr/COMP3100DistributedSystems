""""
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))
message = client_socket.recv(1024)
print("Message from server:", message.decode())
client_socket.close()
"""

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Server info
#client_socket.connect(("localhost", 12345))
server_ip = 'localhost'
server_port= 54323

## Connect to the server
client_socket.connect((server_ip, server_port))

## Receiving incoming message
message = client_socket.recv(1025)
print("Message from server:", message.decode())


# Send a custom message to the server
custom_message = "Hello, server!"
client_socket.sendall(custom_message.encode())

# Receiving the response from the server
response = client_socket.recv(1025)
print("Response from server:", response.decode())


# Closing the connection
client_socket.close()