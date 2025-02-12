class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"Mahsulot, {self.name}, Narx, {self.price}, {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor ")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f" {self.warranty}"
        return data


class Food(Product):
    def __init__(self, name, price, quantity, surok):
        super().__init__(name, price, quantity)
        self.surok = surok

    def info(self):
        data = super().info()
        data += f" || surok, :{self.surok}"
        return data


e = Electronics("Apple", 12, 12, "1 yil", )
print(e.info())
