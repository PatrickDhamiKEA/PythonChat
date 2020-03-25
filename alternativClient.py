import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
your_ip = socket.gethostbyname(socket.gethostname())


def clientSideHandshake():
    send_connection_request = sock.sendto(("com-0 " + your_ip).encode("utf-8"), server_address)

    encoded_response_from_server, server = sock.recvfrom(1024)
    response_from_server = encoded_response_from_server.decode("utf-8")
    server_IP = response_from_server[response_from_server.find('0')+9:]

    try:
        if "com-0 accept" in response_from_server and socket.inet_aton(server_IP):
            send_client_acceptance = sock.sendto("com-0 accept".encode("utf-8"), server_address)
            messageFromServer()
    except:
        print("connection invalid!")
        sock.close()


def messageFromServer():
    first_message_sent = False
    server_response_counter = 0
    while not first_message_sent:
        send_message = sock.sendto(("msg-0=" + input("")).encode("utf-8"), server_address)
        encoded_server_response_to_message, server = sock.recvfrom(1024)
        server_response_to_message = encoded_server_response_to_message.decode("utf-8")
        print(server_response_to_message)
        server_response_counter = int(server_response_to_message[4])
        first_message_sent = True

    while first_message_sent:
        server_message = sock.sendto(("msg-" + str(server_response_counter+1) + "=" + input("")).encode("utf-8"), server_address)
        encoded_server_response_to_message, server = sock.recvfrom(1024)
        server_response_to_message = encoded_server_response_to_message.decode("utf-8")
        print(server_response_to_message)

clientSideHandshake()
