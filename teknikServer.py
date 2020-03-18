import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
sock.bind(server_address)
handshake_done = False
while True:
    data, address = sock.recvfrom(4096)
    print('com-0 <{!r}>'.format(address))
    if data:
        sent = sock.sendto(data, address)
        recv_accept, address2 = sock.recvfrom(4096)
        print('com-0 {}'.format(recv_accept.decode("utf-8")))
        handshake_done = True
    while handshake_done:
        recv_msg, address = sock.recvfrom(4096)
        counter = int('{}'.format(recv_msg.decode("utf-8"))[4])
        print('{}'.format(recv_msg.decode("utf-8")))
        res = sock.sendto(bytes("res-" + str((counter + 1)) + "=" + " I am server", "utf-8"), address)
