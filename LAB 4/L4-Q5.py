class Vehicle:
    def __init__(self, make , model,rent):
        self.make = make
        self.model = model
        self.is_avaliable = True
        self._rent_price = rent
    
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Rent Price: {self.rent_price}")
        status = "Available" if self.is_avaliable == True else status = "Not available"
        print(f"Status: {status}")
    
    def is_rented(self):
        if self.is_avaliable:
            self.is_avaliable = False
            print("You have rented: ")
            self.display()
        else:
            print(f"{self.make} {self.model} is not available")
    
    def is_returned(self):
        if (self.is_avaliable == False):
            self.is_avaliable = True
            print(f"{self.make} {self.model} is now returned and available")

    def calculate_price(self)