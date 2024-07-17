import os
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('x.x.x.x', port_no))
    server_socket.listen(1)
    print("Server is up and listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode()
        if not command or command.lower() == 'exit':
            break
        action, filename = command.split()

        if action == 'upload':
            receive_file(client_socket, filename)
        elif action == 'download':
            send_file(client_socket, filename)
        elif action == 'delete':
            delete_file(client_socket, filename)
        elif action == 'list':
            list_files(client_socket)


    client_socket.close()
    print("Connection closed")

def receive_file(client_socket, filename):
    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

def send_file(client_socket, filename):
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)
    else:
        client_socket.send("File does not exist".encode())

def delete_file(client_socket, filename):
    if os.path.isfile(filename):
        os.remove(filename)
        client_socket.send("File deleted".encode())
    else:
        client_socket.send("File does not exist".encode())

def list_files(client_socket):
    files = os.listdir('.')
    client_socket.send('\n'.join(files).encode())

if _name_ == "_main_":
    start_server()
