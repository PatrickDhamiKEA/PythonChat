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
                messageFromClient()
    except:
        print("connection invalid!")
        sock.close()


def messageFromClient():
    msg_counter = 0
    res_counter = 1
    while True:
        encoded_message_from_client, client_address = sock.recvfrom(4096)
        if msg_counter == 0:
            message_from_client = "msg-" + str(msg_counter) + "=" + encoded_message_from_client.decode("utf-8")
            msg_counter += 1
            print(message_from_client)
            automated_response = sock.sendto(("res-" + str(res_counter) + "=I am server").encode("utf-8"), client_address)

        else:
            message_from_client = "msg-" + str(msg_counter + res_counter) + "=" + encoded_message_from_client.decode("utf-8")
            msg_counter += 1
            print(message_from_client)
            automated_response = sock.sendto(("res-" + str(msg_counter + res_counter) + "=I am server").encode("utf-8"), client_address)
            res_counter += 1


serverSideHandshake()
