class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, number_of_items):
        if number_of_items < 10:

            txt = number_of_items * self.price
            print('{} - {}'.format(self.name, txt))
        elif 100 > number_of_items > 10:

            txt = number_of_items * self.price
            return '{} - {}'.format(self.name, txt * 0.8)
    def make_purchase(self, numbers_of_items):
        self.amount -= numbers_of_items
        return self.amount

x = Product('bag', 100, 10)

x.get_price(20)
x.make_purchase(5)
print(x.amount)
