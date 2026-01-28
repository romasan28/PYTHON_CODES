class address:
    def __init__(self, index_numb, city, street, street_numb, flat_numb):
        self.index_numb = index_numb
        self.city = city
        self.street = street
        self.street_numb = street_numb
        self.flat_numb = flat_numb
    def __str__(self):
        return f"{self.index_numb}, {self.city}, {self.street}, {self.street_numb},{self.flat_numb}"