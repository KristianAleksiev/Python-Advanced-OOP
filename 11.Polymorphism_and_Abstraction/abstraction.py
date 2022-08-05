"""
Abstraction -
- Used to force polymorphism
- Instance cannot be made from an abstract class N.B.!
- An abstract class has AT LEAST 1 abstract method N.B.!
- Created by inheritance of ABC class from abc module
- Abstraction can be achieved by functions and methods, abstract classes
"""
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod  # By doing this, every instance from Class which extends "Animal", MUST overwrite the method
    def make_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Cannot set name less than 2 symbols")
        self.__name = value


class Cat(Animal):
    def __init__(self, name, laziness):
        super().__init__(name)
        self.laziness = laziness

# a = Cat("abv", 3)

    def make_sound(self):  # Enforced polymorphism
        return "Meow"

# a = Cat("abv", 3)

