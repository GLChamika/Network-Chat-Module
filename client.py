import socket

def start_client():
    host = 'localhost'
    port = 8000

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        message = input("Enter message: ")

        # Send the message to the server
        client_socket.send(message.encode())

        # Receive the acknowledgment message from the server
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

    # Close the client socket
    client_socket.close()

if __name__ == '__main__':
    start_client()
