import socket

def start_server():
    host = 'localhost'
    port = 8000

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print("Server started. Waiting for connections...")

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr[0]}:{addr[1]}")

        # Handle client messages
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received message: {message}")
            client_socket.send("Message received".encode())

        # Close the client connection
        client_socket.close()

if __name__ == '__main__':
    start_server()
