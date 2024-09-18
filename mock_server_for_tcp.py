import socket


def server_for_tcp():
    # get hostname
    host = socket.gethostname()
    port = 30105

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    response = "Hello from mock server"
    print("Sending: " + response)
    conn.send(response.encode())

    conn.close()


if __name__ == "__main__":
    server_for_tcp()