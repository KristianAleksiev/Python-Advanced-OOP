class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):  # getter
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):  # setter
        if new_age <= 12:  # Validation as part of encapsulation
            raise ValueError("Only people over 12 are available for age manipulation")
        self.__age = new_age


t = Person("Kris", 25)

print(t.get_age())
print(t.get_name())
# print(t.__name)
