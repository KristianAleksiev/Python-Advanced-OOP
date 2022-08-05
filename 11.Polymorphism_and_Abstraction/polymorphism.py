"""
1. Polymorphism
Ability to present the same interface for differing underlying forms through the interface of their base class
Calling same method, with different operation result
Shape -> Triangle, Square, calculate_area()
Polymorphism is consequence from inheritance with abstraction - Same parent
Avoid the type checking for calling the correct method - > Override the parent's method
Python does not support method overloading like c-like languages, the last defined will be executed - for methods with
the same name inside the class0.

2.Overloading built-in methods - Changing the behavior of functions (str, repr, len etc.)
If a built in method is overloaded the dunder method is called on the left object
__add__ - obj_one + obj_two -> + calls the dunder of obj_one, if the places are switched, may cause a problem ->
obj_two + obj_one - When the objects are from different types

3. Duck typing
Type system used in dynamic languages - same method name, totally different classes
"""

