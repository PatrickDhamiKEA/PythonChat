import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
server_IP = socket.gethostbyname(socket.gethostname())
sock.bind(server_address)


def serverSideHandshake():
    encoded_connection_request_from_client, client_address = sock.recvfrom(1024)
    connection_request_from_client = encoded_connection_request_from_client.decode("utf-8")
    client_IP = connection_request_from_client[connection_request_from_client.find('0') + 2:]

    try:
        if "com-0" in connection_request_from_client and socket.inet_aton(client_IP):
            send_server_acceptance = sock.sendto(("com-0 accept " + server_IP).encode("utf-8"), client_address)
            acceptance_from_client, client_address = sock.recvfrom(1024)
            if "com-0 accept" in acceptance_from_client.decode("utf-8"):
                firstMessageFromClient()
    except:
        print("connection invalid!")
        sock.close()


def firstMessageFromClient():
    encoded_message_from_client, client_address = sock.recvfrom(4096)
    message_from_client = encoded_message_from_client.decode("utf-8")
    print(message_from_client)


serverSideHandshake()
