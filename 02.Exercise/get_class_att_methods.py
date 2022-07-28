class Test:
    test1 = "Class att"

    def __init__(self, name):
        self.name = name
        self.data = []

    def custom(self):
        pass


# Get all methods and attributes

print(dir(Test))
print([x for x in dir(Test) if not x.startswith("_")])
