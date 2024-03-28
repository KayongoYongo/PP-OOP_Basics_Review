from sqlalchemy.ext.declarative import declarative_base

class Employee:
    # Class variables are variables that are shared within each variable of a class
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    """
    After changing the amount in the Developer class, the 
    class instance of Employee does not change
    """
    raise_amount = 1.10

    def __init__(self, first, last, pay, pro_lag):
        super().__init___(first, last, pay)
        self.pro_lag = pro_lag

# ANother example
class Rectangle:
    def __init__(self, **kwargs):
        self.length = kwargs.get('length')
        self.width = kwargs.get('width')

class Square(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.length
        
class Cube(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = kwargs.get('height')

    def volume(self):
        return self.length * self.width * self.height
    
square = Square(length=5)
cube = Cube(length=5, width=5, height=5)

# print(square.area())
# print(cube.volume())

print(dir(declarative_base))
print(None)
print(dir(Rectangle))