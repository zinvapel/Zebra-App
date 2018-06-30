from abc import abstractmethod


class Records:
    @abstractmethod
    def get(self, count=5):
        raise NotImplemented


class Words:
    @abstractmethod
    def get_not_in(self, ids):
        raise NotImplemented
