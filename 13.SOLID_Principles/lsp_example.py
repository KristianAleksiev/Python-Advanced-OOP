class NumbersValidator:
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError(f"Value is out of range [{self.min_value}, {self.max_value}]")  # <============


class NegativeNumbersValidator(NumbersValidator):
    min_value = -1024
    max_value = 0

    def validate(self, value):
        #  Violation of LS principle, different behavior from the parent
        if value < self.min_value or self.max_value < value:
            return False  # <============
        return True  # <============
