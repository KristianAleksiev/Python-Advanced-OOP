"""
Iterator
- An object that can be iterated upon
- An object which returns data, one element at a time

Must implement two methods:
__iter__()
__next__() - iterator protocol

StopIteration exception - Nothing else to iterate


"""

lst = [1, 2, 3, 4, 5]
for x in lst:
    print(x)
"""
At the start of the for loop, the __iter__ is called through iter() upon the lst and returns and iterator
"""

lst_iter = iter(lst)  # Creating an iterator object for lst
print(lst_iter)
print(next(lst_iter))  # Getting the next value

"""Or a manual for loop looks like this
lst_iter = iter(lst)
while True:
    try:
        value = next(lst_iter)
        print(value)
    except StopIteration:
        break
"""

ll = [1, 2, 3, 4, 5]

ll_iter1 = iter(ll)
ll_iter2 = iter(ll)

print(next(ll_iter1))
print(next(ll_iter1))
print(next(ll_iter1))

print(next(ll_iter2))

print(next(ll_iter1))
"""Iterators are independent"""


