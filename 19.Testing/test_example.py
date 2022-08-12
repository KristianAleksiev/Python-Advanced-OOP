from unittest import TestCase


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        return f"My name is {self.fullname} and I am {self.age}-years old!"


#   Testing


class TestPerson(TestCase):
    def test_full_name__expect_to_be_correct(self):
        #  Arrange
        person = Person("Kristian", "Aleksiev", 27)
        #  Act
        actual_fullname = person.fullname
        #  Assert
        expected_fullname = "Kristian Aleksiev"
        self.assertEqual(expected_fullname, actual_fullname)

    def test_get_info__expect_to_be_correct(self):
        person = Person("Kristian", "Aleksiev", 27)
        actual_info = person.get_info()
        expected_info = "My name is Kristian Aleksiev and I am 19-years old!"

        self.assertEqual(expected_info, actual_info)
