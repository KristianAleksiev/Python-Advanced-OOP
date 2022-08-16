# COMMAND PATTERN -
import abc
import sys
from io import StringIO


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass


class AddCommand(Command):
    def execute(self, *args, **kwargs):
        ll, value = args
        ll.append(value)


class SumCommand(Command):
    def execute(self, *args, **kwargs):
        (ll,) = args
        return sum(ll)


class ListCommand(Command):
    def execute(self, *args, **kwargs):
        (ll,) = args
        return ll


sys.stdin = StringIO("""Add 1
Add 2
Sum
List
Add 4
Sum
List
End
"""
                     )
ll = []

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("Add"):
        _, value_str = command.split(" ")
        ll.append(int(value_str))

    elif command == "List":
        print(ll)

    elif command == "Sum":
        print(sum(ll))
