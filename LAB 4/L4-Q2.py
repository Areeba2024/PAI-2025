from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def cal_area(self):
        pass
class rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def cal_area(self):
        return self.l * self.b
class triangle(Shape):
    def __init__(self,h,b):
        self.h = h
        self.b = b
    def cal_area(self):
        return self.h * self.b * 0.5
class square(Shape):
    def __init__(self,l):
        self.l = l
    def cal_area(self):
        return self.l * self.l

s1 = square(3)
r1 = rectangle(2,4)
t1 = triangle(5,10)
print(f"Area of square: {s1.cal_area()}")
print(f"Area of rectangle: {r1.cal_area()}")
print(f"Area of triangle: {t1.cal_area()}")