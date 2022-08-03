class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or roman_map[c] >= roman_map[value[i + 1]]:
                result += roman_map[c]
            else:
                result -= roman_map[c]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            if not isinstance(value, str):
                return "wrong type"

            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)

print(first_num.value)

second_num = Integer.from_roman("IV")

print(second_num.value)

print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))