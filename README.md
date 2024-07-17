# Python Client-Server File-Management-System

## Overview
This project is a simple client-server application for managing files using Python's `socket` and `tkinter` modules. The client can connect to the server and send commands to upload, download, delete, and list files on the server.

## Features
- **Upload**: Upload a file from the client to the server.
- **Download**: Download a file from the server to the client.
- **Delete**: Delete a file from the server.
- **List**: List all files on the server.

## Prerequisites
- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)

## File Structure
- `client.py`: Client-side application with a GUI built using `tkinter`.
- `server.py`: Server-side application.

## Usage

### Server
1. Run the server script:
    ```bash
    python server.py
    ```
    The server will start and listen for client connections.

### Client
1. Run the client script:
    ```bash
    python client.py
    ```
    A GUI will open where you can enter commands.

2. Enter commands in the format:
    ```
    <action> <filename>
    ```
    - **upload**: Upload a file from the client to the server.
    - **download**: Download a file from the server to the client.
    - **delete**: Delete a file from the server.
    - **list**: List all files on the server.

### Example Commands
- Upload a file:
    ```
    upload example.txt
    ```
- Download a file:
    ```
    download example.txt
    ```
- Delete a file:
    ```
    delete example.txt
    ```
- List files:
    ```
    list
    ```

### GUI Features
- **Command Entry**: Enter commands in the text entry field.
- **Send Command**: Click the "Send Command" button to execute the command.
- **Response Display**: The response from the server is displayed in the text area.

## Note
- Ensure the server is running before starting the client.
- The client and server must be on the same network or have network configurations that allow communication between them.

## License
This project is licensed under the MIT License.
