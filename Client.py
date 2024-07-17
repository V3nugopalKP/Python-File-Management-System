import socket
import tkinter as tk
from tkinter import filedialog

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('x.x.x.x', port_no))

    root = tk.Tk()
    root.title("Client")

    def send_command():
        command = entry.get()
        client_socket.send(command.encode())
        if command.lower() == 'exit':
            root.quit()
        action, filename = command.split()

        if action == 'upload':
            send_file(client_socket, filename)
        elif action == 'download':
            receive_file(client_socket, filename)
        elif action == 'delete':
            response = client_socket.recv(1024).decode()
            text.insert(tk.END, response + '\n')
        elif action == 'list':
            print_files(client_socket)

    def print_files(client_socket):
        files = client_socket.recv(1024).decode()
        text.insert(tk.END, files + '\n')

    def send_file(client_socket, filename):
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)

    def receive_file(client_socket, filename):
        with open(filename, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

    entry = tk.Entry(root)
    entry.pack()

    send_button = tk.Button(root, text="Send Command", command=send_command)
    send_button.pack()

    text = tk.Text(root)
    text.pack()

    root.mainloop()

if _name_ == "_main_":
    start_client()
