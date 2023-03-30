import socket
import threading

def send_request(prefix="-"):
    server_address = ('172.18.0.3', 45000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    request = "TIME\r\n"
    client_socket.send(request.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"thread {prefix}", response)
    client_socket.close()

if __name__ == "__main__":
    num_threads = 100
    for i in range(num_threads):
        t = threading.Thread(target=send_request, args=(i,))
        t.start()
