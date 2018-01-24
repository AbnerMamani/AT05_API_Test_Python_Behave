from Data import Data

class Product:

    def __init__(self):
        self.products={}
        self.loadProducts()

    def addProducts(self, cod, item, price, amount):
        d=Data(cod, item, price, amount)
        self.products[cod]=d

    def isAvailableCodProduct(self, cod):
        if cod in self.products:
            return True
        return False

    def discountTheProduct(self,cod, amount):
        self.products[cod].discountAmount(amount)
        return self.products[cod]


    def loadProducts(self):
        self.addProducts("1", "laptop", 500, 40)
        self.addProducts("2", "desktop", 300, 50)
        self.addProducts("3", "hanttop", 100, 70)
        self.addProducts("4", "mouse", 5, 100)
        self.addProducts("5", "keyBoard", 10, 100)
        self.addProducts("6", "display", 100, 0)

    def showProducts(self):
        print("The products are:")
        print("Item : Price : Amount ")
        for key in self.products:
            print(self.products[key].showData())

    def showProductsInStok(self):
        print("The products in stok:")
        print("     cod: Item : Price : Amount ")
        for key in self.products:
            if self.products[key].amount > 0:
                print("     "+self.products[key].showData())


# p= Product()
# # p.loadProducts()
# p.showProducts()
# p.showProductsInStok()