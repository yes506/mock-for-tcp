import socket
from time import sleep

IP = "10.241.238.4"
PORT = 30105
SIZE = 1024
ADDRESS = (IP, PORT)


# configure the server
def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(ADDRESS)
        server_socket.listen()

        while True:
            client_socket, client_address = server_socket.accept()  # 수신 대기
            message = client_socket.recv(SIZE)
            print(f"From {client_address} received: {message}")
            if message:
                client_socket.sendall("Hello, client. I'm a mock server.".encode())
            if message == b'':
                client_socket.sendall("TCP Connection to mock Server established.".encode())
                sleep(3)


if __name__ == "__main__":
    run_server()
