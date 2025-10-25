class Vehicle:
    def __init__(self,capacity):
        self.capacity = capacity
        self.fare = self.capacity * 100

class Bus(Vehicle):
    def __init__(self,capacity):
        super().__init__(capacity)
        self.fare = self.fare + (self.fare * 0.1)
        self.totalFare = self.fare * self.capacity
        self.finalAmount = self.totalFare + (self.totalFare * 0.1)

    def display(self):
        print(f"The total fare is : {self.finalAmount}")

b1 = Bus(100)
b1.display()