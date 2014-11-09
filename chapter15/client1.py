import socket

addr = ('localhost', 8000)
sock = socket.socket()
sock.connect(addr)

while 1:
    data = sock.recv(1024)
    print(data)
    if not data:
        break

# HTTP: server should close at first
sock.close()
