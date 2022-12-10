class Fruit(Inventory):
    
    def __init__(self, item, typeOfFruit, quantity, weight, item_price):
        Inventory.__init__(self, item, typeOfFruit, quantity, weight, item_price)

    def total_price(self):
        total_price_item = self.item_price * self.quantity
        return "Total price of {0}-{1} is ${2}".format(self.item, self.typeOfFruit, total_price_item)

    def discount(self):
        discount = self.item_price*0.95
        return "Today's price after discount for {0}-{1} is ${2}".format(self.item, self.typeOfFruit, discount)

    def sort(self, items = []):
        self.items = items
        return self.items