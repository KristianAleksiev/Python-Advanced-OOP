# TEMPLATE METHOD
import abc


class Sorter(abc.ABC):
    @abc.abstractmethod
    def key_func(self, value):
        pass

    def sort(self, elements):
        return sorted(elements, key=self.key_func)


class NaturalSorter(Sorter):
    def key_func(self, value):
        return value


class ByDivisionRemainderSorter(Sorter):
    def __init__(self, base):
        self.base = base

    def key_func(self, value):
        return value % self.base


ns = NaturalSorter()
rs = ByDivisionRemainderSorter(3)
values = [1, 6, 4, 2, 9]
print(ns.sort(values))
print(rs.sort(values))
