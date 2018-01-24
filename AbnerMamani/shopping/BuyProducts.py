from Products import Products
from Data import Data


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('Test_Log.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


# add the handlers to the logger
logger.addHandler(handler)

#Class that buy the products
class BuyProducts:

    #Constructor that objects of the buy
    #Paramenter products is a object that mangement list of the products
    def __init__(self, products):
        global logger
        logger.debug("initializing product purchases")
        self.products=products
        self.productsBuy = {}

    #Functon that save a buy in a lis of the buy products
    def buyAProduct(self, cod, amount):
        if self.products.isAvailableCodProduct(cod, amount):
            d=self.products.discountTheProduct(cod, amount)
            totalPrice=int(d.price)*int(amount)
            dBuy=Data(d.cod, d.item, totalPrice, amount  )
            self.productsBuy[d.cod]=dBuy
        else:
            print("The amount not is correct")
            logger.debug("The amount not is correct"+ amount)


    #function that execute the buy and interactue wiht user
    def buyAnyProduct(self):
        while True:
            self.products.showProductsInStok()
            print("Please select the cod of product to buy:")
            codProduct=input()
            print("Please into the amount to the buy:")
            amountBuy=input()
            self.buyAProduct(codProduct, amountBuy)
            self.showBuyMade()
            print("Want to continue buying : yes (1) no (any key)")
            buying=input()
            if not buying=="1":
                return


    #function that displayed the list of the buy products
    def showBuyMade(self):
        print("     The buy is:")
        print("         cod: Item : Price : Amount ")
        totalPrice=0
        for key in self.productsBuy:
            print("         "+self.productsBuy[key].showData())
            totalPrice+=self.productsBuy[key].price
        print("         TOTAL PRICE: " +str(totalPrice) )

#Start the execution and loggs
logger.info('Start the execution')
p= Products()
logger.info('Create the Product object')
logger.debug('Records: %s', p)
buy= BuyProducts(p)
buy.buyAnyProduct()
buy.showBuyMade()
p.showProductsInStok()



