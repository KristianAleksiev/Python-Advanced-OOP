def print_list(list):
    print(list)


ll = [1, 2, 3, 4, 5, 6]
print("Printing first list: ")
print_list(ll)

ll2 = [6, 7, 8, 9, 10]
print("Printing second  list: ")
print_list(ll2)
"""
Enables extensibility
If requirements are changed, the change is easily fixable at one place - in the function itself
Easier for debugging, easier for reading
Each function completes a single task (coherent code)
"""