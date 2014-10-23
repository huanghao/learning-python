import re
import sys

from httpserver import serve_forever


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


def index():
    return '<title>Index</title><h1>It works</h1>'


def hello(username):
    # !! NOT SAFE !!
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
