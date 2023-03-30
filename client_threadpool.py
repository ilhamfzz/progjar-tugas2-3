import socket
from concurrent.futures import ThreadPoolExecutor

def send_request(prefix="-"):
    server_address = ('172.18.0.3', 45000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    request = "TIME\r\n"
    client_socket.sendall(request.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"thread {prefix}", response)
    client_socket.close()

if __name__=='__main__':
    executor = ThreadPoolExecutor(max_workers=100)

    for i in range(100):
        executor.submit(send_request, prefix=f"{i}")

    executor.shutdown(wait=True)