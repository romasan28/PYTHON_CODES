class User:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_first_name(self):
        print (self.first_name)
    
    def get_last_name(self):
        print (self.last_name)
    
    def get_firlast_name(self):
        print( f"User: {self.first_name}, {self.last_name}")
