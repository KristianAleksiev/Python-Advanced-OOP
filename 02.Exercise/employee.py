class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


emp1 = Employee(22, "Joro", "Jorkov", 17500)
print(emp1.get_full_name())
print(emp1.get_annual_salary())
print(emp1.raise_salary(500))
