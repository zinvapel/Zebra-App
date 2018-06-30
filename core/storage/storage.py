class MissingElementException(Exception):
    pass


class Storage:
    __list = {}

    @staticmethod
    def set(key, value):
        Storage.__list[key] = value

    @staticmethod
    def get(key, default=None):
        if key in Storage.__list.keys():
            return Storage.__list[key]
        elif default is not None:
            return default

        raise MissingElementException

    @staticmethod
    def remove(key):
        try:
            del Storage.__list[key]
        except KeyError:
            pass

    @staticmethod
    def clear():
        Storage.__list = {}

    @staticmethod
    def update(key):
        return Update(key)


class Update:
    def __init__(self, key):
        self.key = key
        self.val = None

    def __enter__(self):
        self.val = Storage.get(self.key)
        return self.val

    def __exit__(self, exc_type, exc_val, exc_tb):
        Storage.set(self.key, self.val)

    def __getattr__(self):
        return self.val
