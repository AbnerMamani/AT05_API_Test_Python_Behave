from Data import Data

import logging
logging.basicConfig(filename='Test_Log.log',level=logging.DEBUG)
logging.getLogger(__name__)
logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#Class that management the list of te product in the storage
class Products:

    #constructor os the class
    # the initiliza the lis of the products
    # and load values of the products

    def __init__(self):
        self.products={}
        self.loadProducts()

    #Function that add the values in the list of products
    def addProducts(self, cod, item, price, amount):
        d=Data(cod, item, price, amount)
        self.products[cod]=d

    #Verify that the product exist in list of the products
    # and the quantity requested exists
    def isAvailableCodProduct(self, cod, amount):
        if cod in self.products:
            if int(amount) <= self.products[cod].amount:
                return True
        return False

    #function that disconut the amount in the list of the products
    def discountTheProduct(self,cod, amount):
        self.products[cod].discountAmount(amount)
        return self.products[cod]

    #function that load the values to list of the products
    def loadProducts(self):
        logging.info('Load the products ')
        self.addProducts("1", "laptop", 500, 40)
        self.addProducts("2", "desktop", 300, 50)
        self.addProducts("3", "hanttop", 100, 70)
        self.addProducts("4", "mouse", 5, 100)
        self.addProducts("5", "keyBoard", 10, 100)
        self.addProducts("6", "display", 100, 0)

    #Function thata displayed the lis of the all products
    def showProducts(self):
        print("The products are:")
        print("Item : Price : Amount ")
        for key in self.products:
            print(self.products[key].showData())

    # Function thata displayed the lis of the products
    def showProductsInStok(self):
        print("The products in stok:")
        print("     cod: Item : Price : Amount ")
        for key in self.products:
            if self.products[key].amount > 0:
                print("     "+self.products[key].showData())


