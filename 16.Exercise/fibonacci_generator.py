def fibonacci():
    first = 0
    second = 1
    yield first
    yield second

    while True:
        result = first + second
        first, second = second, result
        yield result


generator = fibonacci()

for i in range(10):  # Fibo sequence
    print(next(generator), end=" ")
