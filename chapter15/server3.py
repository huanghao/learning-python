import sys
import socket
import select


def handle_http_client(conn):
    print('HTTP request', conn.recv(1024))

    packet = b'\r\n'.join([
        b'HTTP/1.1 200 OK',
        b'Content-Type: text/html',
        b'',
        b'<h1>Welcome</h1>',
        b'<p>Please wait 3 second ..</p>',
        ])
    conn.send(packet)
    conn.send(b'<p>Bye</p>')


addr = ('localhost', 8000)
sock = socket.socket()
sock.bind(addr)
sock.listen(5)
print('listening on', addr)

reading = [sock, sys.stdin]
running = True

while running:
    rready, wready, eready = select.select(reading, [], [])
    for s in rready:
        if s == sock:
            conn, addr = s.accept()  # Won't block here
            reading.append(conn)
        elif s == sys.stdin:
            msg = sys.stdin.readline()
            if msg == 'quit':
                running = False
            else:
                print('server continue to run ..')
        else:
            handle_http_client(s)
            s.close()
            reading.remove(s)

sock.close()
print('Server down')
