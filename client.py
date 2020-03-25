import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
your_ip = socket.gethostbyname(socket.gethostname())

handshake_done = False

def clientSideHandshake():
    send_connection_request = sock.sendto(("com-0 " + your_ip).encode("utf-8"), server_address)

    encoded_response_from_server, server = sock.recvfrom(1024)
    response_from_server = encoded_response_from_server.decode("utf-8")
    server_IP = response_from_server[response_from_server.find('0')+9:]

    try:
        if "com-0 accept" in response_from_server and socket.inet_aton(server_IP):
            send_client_acceptance = sock.sendto("com-0 accept".encode("utf-8"), server_address)
    except:
        print("connection invalid!")
        sock.close()

clientSideHandshake()
handshake_done = True
while handshake_done:
    send_message = sock.sendto(input("").encode("utf-8"), server_address)

