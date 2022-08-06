class PostgreSQL:
    pass


class StudentsController:
    def __init__(self):
        self.db = PostgreSQL()  # Concrete, only with PostgreSQL objects


class StudentsController2:  # Dependency injection, abstract
    def __init__(self, db):
        self.db = db
