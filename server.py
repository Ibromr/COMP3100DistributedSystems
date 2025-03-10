import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Preperation for receviving incoming connection starts
listen_ip = '0.0.0.0' # 10.125.12.37
listen_port = 54325

#server_socket.bind(("localhost", 12345))
server_socket.bind((listen_ip, listen_port))
server_socket.listen()

#print("Server is listening on port 12345...")
print(f"Server is listening on port {listen_port}")
## Preperation for receviving incoming connection done

while True:
    ## Establish connection wih client
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    ## Send message to the client
    #conn.sendall(b"Hello from server!")
    message = "Hello from server!"
    conn.sendall(message.encode())

     # Receive the client request
    client_request = conn.recv(1024).decode()
    print(f"Received request from client: {client_request}")

    # Process the request and send a custom message
    if client_request == "hello":
        message = "Hello from server!"
    elif client_request == "bye":
        message = "Goodbye from server!"
    else:
        message = "Invalid request"


    # Closing the connection
    conn.close()