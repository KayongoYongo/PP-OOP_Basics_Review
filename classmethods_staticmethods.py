import datetime

class Employee:
    # Class variables are variables that are shared within each variable of a class
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    """
    We use regular methods when you need to work with
    instance-specific data.
    """
    def full_name(self):
        return f'{self.first} {self.last}'

    """
    Class methods can be used as alternative constructors.
    These methods interact with the class.
    The best way to use them is when interacting with
    class level data. In the provided example, the 
    raise amount is the class level data
    """
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    """
    We use static methods when the method doesn't
    depend on the instance or the class state
    """
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return f'The day is a weekend'
        return f'The day is a weekday'

emp_1 = Employee('John', 'Doe', 5000)
emp_2 = Employee('Jane', 'Wu', 5000)

my_date = datetime.date(2024, 3, 29)
# Employee.set_raise_amount(1.05)
print(Employee.is_workday(my_date))