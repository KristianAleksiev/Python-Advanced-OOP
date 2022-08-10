from time import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # <------------------
        start_time = time()

        result = func(*args, **kwargs)

        end_time = time()
        print(f"{func.__name__} executed in {end_time - start_time}")
        return result

    return wrapper


@measure_time
def sum_two(x, y):  # <-------------------
    return x + y


@measure_time
def sum_three(x, y, z):  # <-------------------
    return x + y + z


print(sum_two(1, 2))  # Args=(1, 2)
print(sum_three(1, 2, 3))  # Args=(1, 2, 3)
print(sum_three(1, 2, z=3))  # Args=(1, 2), Kwargs={"z":3}
