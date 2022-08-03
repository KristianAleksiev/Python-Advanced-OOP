class Student:
    def __init__(self):
        self.name = "test"

    def greeting(self):  # Instance method, could be accessed by an object
        return f"Hi! I am {self.name}"


class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):  # No self param, isn't used
        return age >= 18


print(Person.is_adult(5))  # Called by the class
x = Person("Maria")
print(x.is_adult(20))


class StudentTwo:
    kind = "human"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_kind(cls):  # Referring to the class
        cls.kind = "asd"


s1 = StudentTwo("Tester")
s2 = StudentTwo("Tester2")
print(s1.kind)
print(s2.kind)

s1.change_kind()
print(s1.kind)
print(s2.kind)

"""
Static Methods:
@staticmethod
1. It knows nothing about the class or the class instance
2. They could exist outside the class
3. They cannot modify object state or class state
4. Used with the class name mostly, could be called by an instance as well
5. Static methods are independent from everything else around it
6. They help us avoid accidental modifications

Class methods:
@classmethod
1. It is bound to the class, not the object
2. They modify the class state, and apply the change across the instances
3. Used to create new, controlled instances of the class - pre-defining the constructor input

"""


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])  # <----------

    @classmethod
    def quatro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmesan"])  # <---------


first_pizza = Pizza.pepperoni()  # Raising a controlled instance of class Pizza, equivalent to:
# first_pizza = Pizza(["tomato sauce", "parmesan", "pepperoni"])
print(first_pizza.ingredients)
second_pizza = Pizza.quatro_formaggi()
