class Employee:
    # Class variables are variables that are shared within each variable of a class
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        Employee.num_of_emps += 1
    
    """
    By adding the property decorator, we
    are able to access a method as if it was an attribute
    """
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Name Deleted!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Doe')

emp_1.full_name = 'Raiden Omondi'

print(emp_1.email)
print(emp_1.full_name)

del emp_1.full_name

print(emp_1.email)
print(emp_1.full_name)