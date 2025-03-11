import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Preperation for receviving incoming connection starts
listen_ip = '0.0.0.0' # 10.125.12.37
listen_port = 54323

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
    
    
    #client_request = conn.recv(1024).decode("utf-8") #convert bytes to string

    # input message and send it to the client1
    msg = input("Enter message: ")
    conn.sendall(msg.encode("utf-8")[:1024])
    
    
    # if we receive "close" from the client, then we break
    # out of the loop and close the conneciton
    if client_request.lower() == "close":
        # send response to the client which acknowledges that the
        # connection should be closed and break out of the loop
        client_request.send("closed".encode("utf-8"))
        break

    print(f"Received: {client_request}")
    
    

# Closing the connection
conn.close()



''''
It working but you need to refine looping it sends the same message from client to server always: 

ibromr@ibromr5520:~/coding/COMP3100DistributedSystems$ python3 server.py
Server is listening on port 54323
Connection established with ('127.0.0.1', 43986)
Received request from client: heyo  >>>> 1. time
Enter message: yoww
Received: heyo               >>>>>>>>  2. times received 


ibromr@ibromr5520:~/coding/COMP3100DistributedSystems$ python3 client1.py 
Message from server: Hello from server!
Enter message: heyo
Received: yoww



'''






''''
 # Process the request and send a custom message
    if client_request == "hello":
        message = "Hello from server!"
        conn.send(message.encode())
        
        
    elif client_request == "bye":
        message = "Goodbye from server!"
        conn.send(message.encode())

  else:
        message = "Invalid request"
        conn.send(message.encode())  
'''