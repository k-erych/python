class Item:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def __str__(self):
        return f"{self.name}, {self.price} pounds, {self.type}"
class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age} years old."
class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, count in self.products.items():
            total += item.price * count
        return total




