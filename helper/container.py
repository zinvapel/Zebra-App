class Container:
    def __init__(self):
        self.items = {}

    def get_by_id(self, key):
        return self.items[key]

    def add(self, key, value):
        self.items[key] = value
        return self