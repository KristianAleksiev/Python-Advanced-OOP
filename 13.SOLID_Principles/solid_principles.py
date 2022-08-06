"""
More stable code, easier to maintain
Abstract code, predictable

1. Single Responsibility
- Each class is responsible for only one thing and should have only one reason to change
- Less complexity and fragility of the code
- More abstract and more re-usable

2. Open/Closed
- Classes, modules and functions should be open for extension, but closed for modifications
- Modifying the behavior of a class, without directly modifying the class (Inheritance)

3. Liskov Substitution
- Derived types must be completely substitutable for their base types
- Derived classes only extend functionalities of the base class
- Derived classes must not remove base class behavior
- Children must behave like their parents
- Helps create correct hierarchies, polymorphic derived classes

4. Interface Segregation
- A class shouldn't have methods which it doesn't use
- Better to make a few classes with one method each, rather than one class with a lot of methods

5. Dependency Inversion
- Depend on abstractions, not on concretions
"""




