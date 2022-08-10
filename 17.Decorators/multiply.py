def multiply(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return times * func(*args, **kwargs)

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
