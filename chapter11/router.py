import re


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
