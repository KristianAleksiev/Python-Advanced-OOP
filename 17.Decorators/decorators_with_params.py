import sys
from functools import wraps


def dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@dec
def x():
    pass


# decorator factory
def dec_with_params(params):
    def dec(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return dec


@dec_with_params(params=5)
def y():
    pass


#  Example 2

def log(filepath):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            stdout_original = sys.stdout
            with open(filepath, "a") as file: 
                sys.stdout = file
                result = func(*args, **kwargs)
            sys.stdout = stdout_original
            return result
        return wrapper

    return decorator


@log(filepath="./logs.txt")
def say_hello(name):
    print(f"Hello, {name}! How are you?")
