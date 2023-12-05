import socket
import threading

def send_message(client_socket):
    while True:
        # Get user input and send it to the server
        message = input()
        client_socket.send(message.encode('utf-8'))

def receive_message(client_socket):
    while True:
        # Receive messages from the server and print them
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {data}")

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 5555))

    # Start threads for sending and receiving messages
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))

    send_thread.start()
    receive_thread.start()

if __name__ == "__main__":
    start_client()
