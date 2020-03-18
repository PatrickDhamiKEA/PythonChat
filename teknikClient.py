import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
your_ip = socket.gethostbyname(socket.gethostname())

handshake_done = False
counter = 0

try:
    sent = sock.sendto(your_ip.encode("utf-8"), server_address)
    data, server = sock.recvfrom(4096)
    print('com-0 accept <{!r}>'.format(server))

    if data:
        send_accept = sock.sendto("accept".encode("utf-8"), server_address)
        handshake_done = True

    while handshake_done:
        msg = sock.sendto(("msg-" + str(counter) + "=" + input()).encode("utf-8"), server_address)
        counter += 2
        res, server = sock.recvfrom(4096)
        print(res.decode("utf-8"))

finally:
    print('closing socket')
    sock.close()
