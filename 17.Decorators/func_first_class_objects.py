def apply_func_for_list_values(list, func):
    return [func(x) for x in list]


print(apply_func_for_list_values([1, 2, 3], lambda x: x + 2))

"""Concept of decorators - closure"""
def f(x):
    def f_internal(y):
        return x + y

    return f_internal


f1 = f(2)
print(f1)

print(f1(3))
print(f1(5))
