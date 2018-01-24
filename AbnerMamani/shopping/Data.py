#class that creates the structure of a product
class Data:
    def __init__(self, cod, item, price, amount):
        self.cod=cod
        self.item=item
        self.price=price
        self.amount=amount

    #function that shows the values of the class
    def showData(self):
        return f"{self.cod}\t |{self.item} \t | {self.price} \t | {self.amount}"

    #function that dicount the acount of tha product
    def discountAmount(self, discount):
        discount=int(discount)
        if self.amount >= discount:
            self.amount-=discount
            return True
        return False

