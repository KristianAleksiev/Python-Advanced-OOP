"""
Generators
- Way of creating iterators
- A generator is a function that returns an object(iterator)

yield - when dunder next is called, return the value, when next is called again, return the modified value


"""


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


for x in first_n(10):
    print(x)

print(first_n(10))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        yield "name", self.name
        yield "age", self.age
        # return (pair for pair in self.__dict__.items())


me = Person("Kristian", 27)

for x in me:
    print(x)

"""Generator expressions"""


def gen_func(n):
    for x in range(n):
        yield x


def print_values(values_iter):
    for value in values_iter:
        print(value)


# [ literal for list comprehension
# { literal for dict comprehension
# ( literal for generator expression

print_values(gen_func(5))

print_values(x for x in range(5))


