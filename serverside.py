import socket
import threading

def handle_client(client_socket, address):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break  # If no data is received, exit the loop

        print(f"Received from {address[0]}:{address[1]}: {data}")

        # Send the received data back to the client
        client_socket.send(data.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('0.0.0.0', 5555))

    # Enable the server to accept connections (maximum 5 connections in the queue)
    server_socket.listen(5)

    print("Server listening on port 5555")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Create a new thread to handle the client's messages
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
