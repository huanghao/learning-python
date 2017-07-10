import time
import socket

addr = ('localhost', 8000)
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(addr)
sock.listen(5)
print('listening on', addr)

while True:
    conn, addr = sock.accept()
    print('new client', addr)
    packet = b'\r\n'.join([
        b'HTTP/1.1 200 OK',
        b'Content-Type: text/html',
        b'',
        b'<h1>Welcome</h1>',
        b'<p>Please wait 3 second ..</p>',
        ])
    conn.send(packet)
    time.sleep(3)
    conn.send(b'<p>Bye</p>')
    conn.close()
    print('disconnect client')
