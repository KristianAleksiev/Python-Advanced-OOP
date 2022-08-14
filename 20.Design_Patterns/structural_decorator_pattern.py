import abc
import json


class DataExporter(abc.ABC):
    @abc.abstractmethod
    def export(self, data):
        pass


class JsonDataExporter(DataExporter):
    def export(self, data):
        return json.dumps(data.__dict__)


class StringDataExporter(DataExporter):
    def export(self, data):
        return str(data)


class EncryptDataExporter(DataExporter):
    """DECORATOR PATTERN PRINCIPLE"""
    def __init__(self, exporter):
        self.exporter = exporter

    def __encrypt(self, value):
        return f"--{value}--"

    def export(self, data):
        for key in data.__dict__.keys():
            value = getattr(data, key)
            encrypted_value = self.__encrypt(value)
            setattr(data, key, encrypted_value)
        return self.exporter.export(data)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


exporter = EncryptDataExporter(JsonDataExporter())
cat = Cat("Pepa", 4)
print(exporter.export(cat))
