from upper_main import BaseStorage
from upper_main import AbstractionStorage


class Store(BaseStorage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int):
        if self.get_unique_items_count() >= 5:
            print("Слишком большой ассортимент")
            raise Exception
        super().add(title, quantity)


class Request:
    def __init__(self, request: str, storages: dict):
        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise Exception

        self.amount = int(splitted_request[1])
        self.product = splitted_request[2]
        self.carry_from = splitted_request[4]
        self.take_to = splitted_request[6]

        if self.carry_from not in storages or self.take_to not in storages:
            raise Exception
