from abc import ABC, abstractmethod


class AbstractionStorage(ABC):
    @abstractmethod
    def add(self, title, quantity):
        pass

    @abstractmethod
    def remove(self, title, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class BaseStorage(AbstractionStorage):
    def __init__(self, items: dict, capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, title: str, quantity: int):
        if self.get_free_space() < quantity:
            raise Exception
        else:
            if title in self.__items.keys():
                self.__items[title] += quantity
            else:
                self.__items[title] = quantity

    def remove(self, title: str, quantity: int):
        if self.__items[title] < quantity:
            raise Exception
        elif self.__items[title] == quantity:
            del self.__items[title]
        else:
            self.__items[title] -= quantity

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
