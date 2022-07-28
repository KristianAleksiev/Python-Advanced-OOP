class Person:
    """Creates a glass object
     Properties:
        - Name and age
     Methods:
         print_info:
            - Prints the information about an object
     """
    MIN_AGE = 0  # Data attribute, Class data attribute

    def __init__(self, name, age):  # Function attribute
        self.name = name  # Instance data attribute
        self.age = age

    def print_info(self):
        """Printing the information about the current object"""
        print(f"I am {self.name} and I am {self.age} years old")

    def __str__(self):
        return f"Object '{self.name}' from class 'Person' with min age of {self.MIN_AGE}"


p1 = Person("Joro", 20)
p2 = Person("Maria", 32)
print(Person.print_info)
print(Person.MIN_AGE)

p1.print_info()
Person.print_info(p1)

print(str(p1))
# print(repr(p1))
Person.MIN_AGE = 13
print(p1)
print(p2)
p2.MIN_AGE = 15
print(str(p2))
print(p1)
print(Person.__doc__)
print(Person.print_info.__doc__)
print(p1.__doc__)
print(p2.__dict__)


"""
Classes are not built-in, they are added as sugar to functions
__init__ - Specifies the initial state of the class instance 

self - reference to the instance inside the instance 

__str__ - String representation of an object
__repr__ - Machine readable representation ("")

Not a good practice to change class attributes dynamically, usually used as constants

Classes and funcs in Python are first-class citizens (they also are objects)

__dict__ - Gets the instance attributes dynamically - State of the object as a dictionary
"""
