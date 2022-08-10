"""
def uppercase(func_to_decorate):
    result = func_to_decorate()
    return result.upper()


def uppercase_decorator(func_to_decorate):  # The decorator
    def func_wrapper():
        result = func_to_decorate()
        return result.upper()

    return func_wrapper


def get_shopping_list():
    return "eggs, milk, pizza"


def get_name():
    return "Kristian Aleksiev"


print(f"I am {get_name()}")
print(f"I am {uppercase(get_name)}")

print(f"I have to buy {get_shopping_list()}")
print(f"I have to buy {uppercase(get_shopping_list)}")

print(uppercase(get_shopping_list))
print(uppercase(get_name))

print(10 * "-")

get_name = uppercase_decorator(get_name)  # The decorating of get_name()
print(f"I am {get_name()}")

Correct python syntax:
"""


def uppercase_decorator(func_to_decorate):  # The decorator
    def func_wrapper():
        result = func_to_decorate()
        return result.upper()

    return func_wrapper


@uppercase_decorator
def get_shopping_list():
    return "eggs, milk, pizza"


@uppercase_decorator
# syntax sugar of get_name = uppercase_decorator(get_name)
def get_name():
    return "Kristian Aleksiev"


print(f"I am {get_name()}")
print(f"I have to buy {get_shopping_list()}")
print(get_name.__name__)

from functools import wraps


def uppercase_decorator2(func_to_decorate):  # The decorator @wraps
    # - correct func name, docstrings etc instead of wrapper
    @wraps(func_to_decorate)
    def func_wrapper():
        result = func_to_decorate()
        return result.upper()

    return func_wrapper


@uppercase_decorator2
def get_name():
    return "Kristian Aleksiev"


print(get_name.__name__)
