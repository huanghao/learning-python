
class Proxy:

    def __init__(self, wrapped):
        self.__dict__['_wrapped'] = wrapped

    def __getattr__(self, name):
        return getattr(self._wrapped, name)

    def __setattr__(self, name, value):
        if name == '_wrapped':
            raise AttributeError("Access denied")
        if hasattr(self._wrapped, name):
            return setattr(self._wrapped, name, value)
        return object.__setattr__(self, name, value)

    def __len__(self):
        return len(self._wrapped)

    def __getitem__(self, key):
        return self._wrapped[key]

    def __setitem__(self, key, value):
        self._wrapped[key] = value

    def __delitem__(self, key):
        del self._wrapped[key]

    def __contains__(self, item):
        return item in self._wrapped

