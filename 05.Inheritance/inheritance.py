"""
Basic concepts of OOP

1. Inheritance - Capability to inherit other classes' properties and methods
- Extend the functionality of the code's existing classes to eliminate repetitive code

2. Encapsulation
- Stop objects from interacting with each other so classes cannot change or
interact with the specific variables and functions of an object

3. Abstraction
- Isolate the impact of changes made to the code so the change will only affect
the variables shown and not the outside code

4. Polymorphism
- Allows different classes to use methods with the same name


Benefits of Inheritance:
- Code re-usability
- Add features to a class without modifying it
- Transitive in nature
"""


class Person:  # Person is extended by Teacher
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"{self.name}, {self.age}")


class Teacher(Person):  # Teacher extends Person
    def teach(self):  # Adding a behavior without modifying the base
        print(f"{self.name} is teaching")


t = Teacher("Pesho", 45)
t.get_info()
print(t.name)
print(t.age)
t.teach()

"""
The super() method

- Built-in method which returns a temporary object of the superclass
- Allows you to call methods of the superclass in your subclass
- The primary use case of this is to extend the functionality of the inherited method
- Used in the class that inherits from another, manipulating the Parent class state or behavior,
when both classes have same
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(Person):
    def __init__(self, name, age, subject, title):
        super().__init__(name, age)  # Go to Person, set name and age, come back and finish setting this C objects' init
        # super(Teacher, self).__init__(name, age) -  Older versions of python
        self.subject = subject
        self.title = title

    def teach(self):
        print(f"{self.title}. {self.name} is teaching {self.subject}")

    def __str__(self):
        # parent_str = super().__str__()
        return f"{super().__str__()}; Subject: Python OOP"
    #   Parent str + modification


a = Person("P", 12)
# t = Teacher("Kristian", 28)
t1 = Teacher("Maria", 47, "Python OOP", "Mrs")
t2 = Teacher("Joro", 37, "JavaScript", "Mr")
# print(t)
print(a)  # Parent behavior not changed
t1.teach()
t2.teach()

"""
Types of inheritance:
1. Single - Parent(base) - Child(extends)
 
2. Multiple - When a child inherits from more than one parent class C(A, B)
When same method exists in both parents, when the method is called, the method from the first parent is executed - 
The order of Inheritance is important
Super() reference to FIRST parent in the inheritance
X.__init__(self, name)
Y.__init__(self, age)
Could be done but explicitly

3. Multilevel -  A, B(A), C(B)
Child inherits from Parent, which inherits from Grandparent

4. Hierarchical
When a number of classes inherit from the same parent A, B(A), C(A), D(A)

----------------------------------------------------------

Method Resolution Order (Python 3):
- Order in which methods should be inherited in the presence of multiple inheritance
- In python 3 C3 Linearization algorithm is used for MRO
- It is possible to see MRO of a class using mro() method of the class

A - B - C(A, B)
print(C.mro())
1. Search if method exists in current class(C)
2. If not search in parent class (A)
3. If not search in parent class (B)
4. If not search in class (object)

----------------------------------------------------------

Mixins
- A mixin is a class that is implementing a specific set of features that is needed in many different classes
- A mixin is a class which has no data, only methods
- Mixins cannot be instantiated by themselves
- They are used to extend functionality - to be inherited
- They allow inheritance and use of only desired features from the parent class, not all of them
Example:
"""


class StrMixin:
    def __str__(self):
        return ";".join(f"{key}={value}" for key, value in self.__dict__.items())


class Person(StrMixin):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    # def __str__(self):
    #     return ";".join(f"{key}={value}" for key, value in self.__dict__.items())


class Building:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    # def __str__(self):
    #     return ";".join(f"{key}={value}" for key, value in self.__dict__.items())


print(Person("X", 12))
print(Building("UNSS", "Stud grad"))