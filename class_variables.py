class Employee:
    # Class variables are variables that are shared within each variable of a class

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        # If we use the below line of code, we will get a name error
        # self.pay =  int(self.pay * raise_amount)
        # The proper way of doing it is through
        """
        For us to access the class variables,
        we need to access them through the class itself
        or an instance of the class
        """
        # self.pay =  int(self.pay * Employee.raise_amount)
        # or
        self.pay =  int(self.pay * self.raise_amount)

        # If these are class variables, why can we access them from our instances?
        """
        if we try to access an attribute on an instance, it will first check if 
        the instance contains the attribute. And if it doesn't it will check
        if the class or any class it inherits from has it.
        """
print(Employee.num_of_emps)
emp_1 = Employee("Sam", "John", 5000)
emp_1 = Employee("Dan", "John", 5000)
emp_1 = Employee("Paul", "John", 5000)
# print(emp_1.pay)
"""
If we call the function without using the bracket and print it,
the print statement will return the location of the function object
in the memory.
"""
# print(emp_1.apply_raise)
emp_1.apply_raise()

# print(emp_1.__dict__)
# This line will show that the raise amount is avilable to the intance of the class
# print(dir(emp_1))

# We can overide the raise amount for a specific instance
# The value will be the specific value for the emp_1
# emp_1.raise_amount = 1.05
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# 
print(Employee.num_of_emps)