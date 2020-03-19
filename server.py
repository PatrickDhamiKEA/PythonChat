import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
server_IP = socket.gethostbyname(socket.gethostname())
sock.bind(server_address)

handshake_done = False

while True:
    data, address = sock.recvfrom(1024)
    incoming_IP = data.decode("utf-8").split(".")
    accepted_IP = ""
    #itererer igennem de dele der burde være en IP, hvis ikke det er tal vil try/except blokken fange det, og hvis ikke det er tal imellem 0 og 999 vil if/else blokken fange det
    for i in incoming_IP:
        try:
            if 0 <= int(i) <= 999:
                accepted_IP += i + "."
            else:
                print("not a valid IP")
                send_decline_message = sock.sendto("declined".encode("utf-8"), address)
                break
        except:
            print("not a valid IP!")

    print("C: com-0 <" + accepted_IP[0:-1] + ">")
    while True:
        send_acceptance = sock.sendto(server_IP.encode("utf-8"), address)

while True:
    receive_client_accept, address = sock.recvfrom(1024)
    print("C: com-0 " + receive_client_accept)

    """recv_accept, address2 = sock.recvfrom(4096)
    print('com-0 {}'.format(recv_accept.decode("utf-8")))
    handshake_done = True

    while handshake_done:
        recv_msg, address = sock.recvfrom(4096)
        counter = int('{}'.format(recv_msg.decode("utf-8"))[4])
        print('{}'.format(recv_msg.decode("utf-8")))
        res = sock.sendto(bytes("res-" + str((counter + 1)) + "=" + " I am server", "utf-8"), address)
        """
