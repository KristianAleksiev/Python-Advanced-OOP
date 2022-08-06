class NumbersValidator:
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError(f"Value is out of range [{self.min_value}, {self.max_value}]")


class NegativeNumbersValidator(NumbersValidator):
    min_value = -1024
    max_value = 0


# Example 2
""""
class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        # OCP Violation
        if self.average_grade > 5:
            return self.semester_tax * 0.6

        elif self.average_grade > 4:
            return self.semester_tax * 0.8
            
Fixed, without violations
"""


class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.6
        return 0  # <=======


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()

        if result > 0:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2
        return 0  # <=======
