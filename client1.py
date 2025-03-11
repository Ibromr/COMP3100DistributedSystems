import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Server info
#client_socket.connect(("localhost", 12345))
server_ip = 'localhost'
server_port= 54323

## Connect to the server
client_socket.connect((server_ip, server_port))

while True:
    ## Receiving incoming message
    message = client_socket.recv(1024)
    print("Message from server:", message.decode())

    # input message and send it to the server
    msg = input("Enter message: ")
    client_socket.send(msg.encode("utf-8")[:1024])

    # receive message from the server
    response = client_socket.recv(1024)
    response = response.decode("utf-8")

    # if server sent us "closed" in the payload, we break out of the loop and close our socket
    if response.lower() == "closed":
        break

    print(f"Received: {response}")

# Closing the connection
client_socket.close()