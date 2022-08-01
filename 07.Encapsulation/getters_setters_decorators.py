class Person:
    def __init__(self, age=0):
        self.age = age  # Same name,  if it is self.__age,
        # it will skip the setter and the getter, treats it like another variable

    @property
    def age(self):  # Same name
        return self.__age  # <---- creating a private variable, recursion avoided

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age

    @property
    def test(self):
        return "Hello"


p = Person(16)
print(p.age)  # When called it is referenced to the getter, so it returns the age

p.age = 22  # When is manipulated it is referenced to the setter, so it is being validated and set
print(p.age)
print(p.test)  # Called without (), as a reference of an attribute
"""
@property decorator, given a method, it is being called without ()
When an attribute is being initialized to an instance and a setter decorator is available,
 before passing the value, it moves through the setter, it is validated and a value is passed
"""