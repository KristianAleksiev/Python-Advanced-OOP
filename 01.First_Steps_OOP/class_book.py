class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):  # User, __repr__ machine
        return f"{self.author}, {self.pages}, {self.name}"


b = Book("Harry Potter and GoF", "J.K. Rowling", 500)

print(b.author)
print(b.name)
print(b.pages)

print(b)