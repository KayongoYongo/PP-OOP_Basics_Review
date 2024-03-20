class Animal:
    def __init__(self, first, last, color, age):
        self.first = first
        self.last = last
        self.color = color
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    """
    If you want to print more meaningful information about the objects, 
    you should override the __str__ method in the Animal class 
    to customize the string representation of the objects
    """
    def __str__(self) -> str:
        return f"{self.first}  is a {self.color} animal, and it's {self.age} years old."

cat = Animal('Gandalf', 'The cuteness','brown', 10)
dog = Animal('Rafiki', 'The bodld','black', 5)

"""
If we print the instances without defining the ___str__ method,
we will end up printing the memory location of the object
"""

# print(cat)
# print(dog)

print(cat.full_name) # Without the bracket, I am printing a reference to the function object itself
print(cat.full_name())