from datetime import date, timedelta

class Inventory:

    def __init__(self, item, typeOfFruit, quantity, weight, item_price):
        self.item = item
        self.typeOfFruit = typeOfFruit
        self.quantity = quantity
        self.weight = weight
        self.item_price = item_price

    def update(self, fruit_item):
        self.fruit_item = fruit_item

    def expiry(self):
        return "Expiry date of fruit - {0}".format(date.today() + timedelta(days=7))
    
    def display(self):
        return "Fruit - {0}, Type of Fruit - {1}, Total Quantity - {2}, Weight - {3} kgs, Price of item - ${4}".format(self.item, self.typeOfFruit, self.quantity, self.weight, self.item_price)