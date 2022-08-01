"""
Encapsulation definition - Data in class protected outside the class, packing the state and behaviour.
Includes data protection but validation as well.
Prevents accidental modifications of data.
The data in the class could be manipulated only by accessing one of its class methods.

Everything in python is public by default.

Access modifying:
__private and _protected behavior and state

Getter and setter - Accessing private attributes and methods
- through decorators

"""


class Student:

    def __init__(self, number, id):
        self.number = number
        self.__id = id
        self._grades = [3, 4]

    def calculate_age(self):
        year = self.__id[:2]


student = Student("131263", "20010204")
print(student.number)
# print(student.__id)  # Private outside the class
print(student._Student__id)  # Still private, but accessible obj._Class__attribute
print(student._grades)  # Protected, accessible by the class and its inheritants

"""
Built in functions for checking attributes:

getattr() - used to access the attribute of an object
print(getattr(object, "searched att")

hasattr() - checks if an attribute exists or not
print(hasattr(object, "searched attribute")

setattr() - used to set the value of the attribute - person.age = 15
delattr() - deletes an attribute INSIDE THE INSTANCE
"""