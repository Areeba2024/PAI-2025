class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculateBonus(self):
        pass

class Manager(Employee):
    def calculateBonus(self):
        return self.salary * 0.20

    def hire(self):
        print(f"{self.name} is hiring a new employee.")


class Developer(Employee):
    def calculateBonus(self):
        return self.salary * 0.10

    def writeCode(self):
        print(f"{self.name} is writing code.")


class SeniorManager(Manager):
    def calculateBonus(self):
        return self.salary * 0.30

manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
senior_manager = SeniorManager("Carol", 100000)

print(f"{manager.name}'s bonus: ${manager.calculateBonus():,.2f}")
print(f"{developer.name}'s bonus: ${developer.calculateBonus():,.2f}")
print(f"{senior_manager.name}'s bonus: ${senior_manager.calculateBonus():,.2f}")

manager.hire()
developer.writeCode()
