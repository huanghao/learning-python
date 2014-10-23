import re
import os
import sys
import socket
import datetime


def Router(rules):
    """
    `rules` is a sequence of pairs like (pattern, handler).

    This function returns a router which accepts a url, returns
    corresponding handler and its arguments.

    If there are more than one pattern can match a url, the first
    one that matched will be used.
    """
    rules = [(re.compile(p), h) for p, h in rules]

    def dispatcher(url):
        """
        Call handler that match the `url`. Values of matched
        groups will be passed as arguments.
        """
        for regex, handler in rules:
            match = regex.fullmatch(url)
            if match:
                return handler, match.groups(), match.groupdict()

    return dispatcher


def readline(conn):
    buf = []
    while 1:
        chunk = conn.recv(64)
        #print('chunk:', chunk)
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


def index():
    return '<title>Index</title><h1>It works</h1>'


def hello(username):
    #!! NOT SAFE !!
    return '<p>Nice to meet you <strong>{}</strong> !</p>'.format(username)


def about():
    return """It's just a very simple demo for web server"""


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    address = ('localhost', port)
    router = Router((
        ('/', index),
        ('/hello/(?P<username>\w+)', hello),
        ('/about', about),
        ))

    serve_forever(address, router)
