class Student():
    def __init__(self,name,id):
        self.name = name 
        self.id = id
    def display(self):
        print(f"Name: {self.name} \nID: {self.id}")

class Marks(Student):
    def __init__(self, name, id,algo,dsa,cal):
        super().__init__(name, id)
        self.algo = algo
        self.dsa = dsa
        self.cal = cal
    
    def display(self):
        super().display()
        print(f"Algorithms: {self.algo}")
        print(f"DSA: {self.dsa}")
        print(f"Calculus: {self.cal}")
class Result(Marks):
    def __init__(self, name, id, algo, dsa, cal):
        super().__init__(name, id, algo, dsa, cal)
    
    def calculate(self):
        total = self.algo + self.cal + self.dsa
        avg = total/3
        return total,avg
    
    def display(self):
        super().display()
        total,avg = self.calculate()
        print(f"Total: {total}")
        print(f"Average: {avg}")



std = Result("Asma",23433,67,78,89)
std.display()