# Build an object part by part, Abstraction on factory

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ", ".join(f"{key} - {value}" for key, value in self.__dict__.items())


class PersonBuilder:
    """COULD BE SET DEFAULT VALUES"""
    person_attrs = {
        "name": "Default",
        "age": 0
    }

    def set_name(self, name):
        self.person_attrs["name"] = name

    def set_age(self, age):
        self.person_attrs["age"] = age

    def build(self):
        """Could be used for validation"""
        return Person(**self.person_attrs)


builder = PersonBuilder()
# builder.set_age(29)
builder.set_name("Kristian")
print(builder.build())
