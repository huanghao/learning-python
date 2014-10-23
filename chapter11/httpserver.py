import os
import sys
import socket
import datetime


def readline(conn):
    buf = []
    while 1:
        chunk = conn.recv(64)
        # print('chunk:', chunk)
        if not chunk:
            break
        buf.append(chunk)
        if b'\n' in chunk:
            break
    return b''.join(buf)


def serve_forever(address, router):
    """
    Lauch a http server at `address`
    """
    def process_request(request_line):
        method, url, protocol = request_line.split()

        res = router(url.decode())
        if res:
            status = protocol + b' 200 OK'
            handler, args, kwargs = res
            if kwargs:
                body = handler(**kwargs)
            else:
                body = handler(*args)
            body = body.encode()
        else:
            status = protocol + b' 404 Not Found'
            body = b'Page not found'
        return status, body

    # Parent
    sock = socket.socket()
    sock.bind(address)
    sock.listen(5)
    print('listen on {} ...'.format(address))

    while 1:
        try:
            conn, address = sock.accept()
        except KeyboardInterrupt:
            print('cleanup and exit ...')
            sock.close()
            break

        if os.fork() == 0:
            sock.close()
            try:
                request_line = readline(conn).split(b'\r\n', 1)[0]
                status, body = process_request(request_line)

                print('{}:{}:{}: {} => {}'.format(
                    datetime.datetime.now(), os.getpid(), address,
                    request_line.decode(), status.decode(),
                    ))

                response = b''.join([
                    status, b'\r\n',
                    b'Content-Type: text/html\r\n\r\n',
                    body,
                    ])
                conn.send(response)
            finally:
                conn.close()
            sys.exit(0)
        else:
            conn.close()
