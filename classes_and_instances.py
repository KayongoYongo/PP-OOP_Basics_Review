"""When creating a class, it is a good practice to name the class by starting with a capital letter"""
class Animal:
    # After creating a class, it cannot be left empty.
    # If you do not want to pass any value into it, add the word pass
    pass

# Notes
# A class is basically a blueprint for creating instances
cat = Animal()
dog = Animal()

# Each of the above instances is a unique object created from the class Animal
print(cat) # <__main__.Animal object at 0x0000021938384910>
print(dog) # <__main__.Animal object at 0x0000021938384950>
# From the above print statment, it shows that each object is unique and is stored at a different location

# Instance variables contain data that is unique to each instance
cat.name = "Munchkins"
cat.color = "Black"
cat.age = 10

print(cat.name)
# If the dog attribute has not been defined, we will get an attribute error
print(dog.name) # AttributeError: 'Animal' object has no attribute 'name'