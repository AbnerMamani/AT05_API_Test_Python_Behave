class Dictionary_users:
    def __init__(self):
        self.dict_name={}
        self.dict_price={}
        self.load_dictionary_by_nane()
        self.load_dictionary_by_price()


    def load_dictionary_by_nane(self):
        self.dict_name[1] = "Carlos"
        self.dict_name[2] = "Pinocho"
        self.dict_name[3] = "Julia"
        self.dict_name[4] = "Julio"
        self.dict_name[5] = "Carlos"


    def load_dictionary_by_price(self):
        self.dict_price[1] = 50
        self.dict_price[2] = 100
        self.dict_price[3] = 200
        self.dict_price[4] = 500
        self.dict_price[5] = 10

    def get_dictionary_by_price(self):
        return self.dict_price

    def get_dictionary_by_name(self):
        return self.dict_name

    def search_id_by_name(self, name, id):
        for key in self.dict_name:
            if self.dict_name[key] == name and key == id:
                return key

    def search_id_by_price(self, price, id):
        for key in self.dict_price:
            if self.dict_price[key] == price and key == id:
                return id
