import socket
import threading


print("[+] Server Running ...")
HOST = "127.0.0.1"
PORT = 1402

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("[+] Server Listening on %s:%d" % (HOST, PORT))

clients = []
def handle_client(client_socket, address):
    print(f"[+] Connected client: {address}")
    clients.append(client_socket)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        for client in clients:
            if client != client_socket:
                client.send(data)

    print(f"[+] Connection closed with client: {address}")
    clients.remove(client_socket)
    client_socket.close()
while True:
    client_socket, address = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
