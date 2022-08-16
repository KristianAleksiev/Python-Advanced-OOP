# TEMPLATE METHOD
import abc


class SortStrategy(abc.ABC):
    @abc.abstractmethod
    def get_key_func(self, *args, **kwargs):
        pass


class NaturalSortStrategy(SortStrategy):
    @staticmethod
    def __key_func(value):
        return value

    def get_key_func(self, *args, **kwargs):
        return self.__key_func


class DivisionRemainderStrategy(SortStrategy):
    def __init__(self, base):
        self.base = base

    def __key_func(self, value):
        return value % self.base

    def get_key_func(self, *args, **kwargs):
        return self.__key_func


class Sorter:
    sort_strategy = NaturalSortStrategy()

    def sort(self, elements):
        return sorted(elements, key=self.sort_strategy.get_key_func())


s = Sorter()
values = [1, 5, 3, 9]
print(s.sort(values))
s.sort_strategy = DivisionRemainderStrategy(3)
print(s.sort(values))
