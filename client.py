import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
your_ip = socket.gethostbyname(socket.gethostname())

handshake_done = False
counter = 0

#sending IP for acceptance by server
send_request = sock.sendto(your_ip.encode("utf-8"), server_address)

connection_message, server = sock.recvfrom(1024)
if connection_message.decode("utf-8") == "declined":
    print("connection declined!")
    sock.close()
try:
    server_acceptance, server = sock.recvfrom(1024)
    print("S: com-0 accept <" + server_acceptance.decode("utf-8") + ">")
    handshake_done = True

except:
    print("connection closing")
    sock.close()

while handshake_done:
    send_accept_of_accept = sock.sendto("accept".encode("utf-8"), server_address)

"""data, server = sock.recvfrom(4096)
    print('com-0 accept <{!r}>'.format(server))

    if data:
        send_accept = sock.sendto("accept".encode("utf-8"), server_address)
        handshake_done = True

    while handshake_done:
        msg = sock.sendto(("msg-" + str(counter) + "=" + input()).encode("utf-8"), server_address)
        counter += 2
        res, server = sock.recvfrom(4096)
        print(res.decode("utf-8"))"""


