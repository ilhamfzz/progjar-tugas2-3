import socket
import threading
from datetime import datetime

def handle_request(client_socket):
    request = client_socket.recv(1024).decode()
    if request.startswith("TIME") and request[4:6] == "\r\n":
        now = datetime.now().strftime("%H:%M:%S")
        response = f"JAM {now}\r\n"
        client_socket.send(response.encode())
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 45000)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"Server is listening on {server_address}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        t = threading.Thread(target=handle_request, args=(client_socket,))
        t.start()

if __name__ == "__main__":
    start_server()