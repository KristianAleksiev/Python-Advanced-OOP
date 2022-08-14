"""
They manage problems with abstraction when initializing objects

- Encapsulating knowledge about which classes the system uses
- Hiding how instances of these classes interact

List of creational patterns:
- Singleton - Only one instance is generated, no matter how many objects we create, inheritance problem
- Simple factory - All factories have a method which creates an object
- Factory method
- Abstract factory
- Builder - Create objects by piece
- Object pool - Pool of workers, if a problem occurs, take one worker, he fixes it and goes in the pool again
- Prototype
- Lazy initialization - Intent to use an object, when there is need is initialized, used with databases
- Fluent interface

Factories - Abstraction on top of constructors
Builders - Abstraction on top of factories
"""
import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_noise(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        pass


class Dog(Animal):
    def __init__(self, name):
        pass


"""
cat Gosho 7
dog Pesho 
cat Tigyr 11
"""


#
# while True:
#     type, *others = input().split()
#     if type == "cat":
#         Cat(*others)
#     else:
#         Dog(*others)
#
# while True:  # Abstraction of creating of the objects
#     type, *others = input().split()
#     animal = animals_factory.create(type, *others)
#


