# CHAIN OF RESPONSIBILITY
import abc


class Handler(abc.ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle(self, *args, **kwargs):
        pass


class IntsHandler(Handler):
    def handle(self, value):
        if not isinstance(value, int):
            return self.next_handler.handle(value)
        return f"{value} is int"


class FloatsHandler(Handler):
    def handle(self, value):
        if not isinstance(value, float):
            return self.next_handler.handle(value)
        return f"{value} is float"


root_handler = IntsHandler()
root_handler.next_handler = FloatsHandler()

value = 1
print(root_handler.handle(value))
value = 1.2
print(root_handler.handle(value))
