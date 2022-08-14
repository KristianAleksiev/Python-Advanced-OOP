# SIMPLE FACTORY PATTERN
import abc
import json


class Cat:
    kind = "cat"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog:
    kind = "dog"

    def __init__(self, name):
        self.name = name


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


type = "json"  # | str


# de = None


def create_data_exporter(type):
    """ SIMPLE FACTORY """
    if type == "json":
        return JsonDataExporter()
    else:
        return StringDataExporter()


# if type == "json":
#     de = JsonDataExporter()
# else:
#     de = StringDataExporter()
#


de = create_data_exporter(type)

animals = [
    Dog("Sharo"),
    Cat("Bleki", 12)
]

[print(de.export(animal)) for animal in animals]


# ==================================================================================

# FACTORY METHOD


class DataExporterFactory:
    json_exporter = None
    string_exporter = None

    def create_exporter(self, type):
        """FACTORY METHOD"""
        if type == "json":
            if self.json_exporter is None:
                self.json_exporter = JsonDataExporter()

            return self.json_exporter
        return StringDataExporter()


factory = DataExporterFactory()
de = factory.create_exporter(type)

[print(de.export(animal)) for animal in animals]


# ==================================================================================

# ABSTRACT FACTORY

class DataExporterFactoryAbstract(abc.ABC):
    @abc.abstractmethod
    def create_exporter(self):
        pass


class JsonExporterFactoryAbstract(DataExporterFactoryAbstract):
    exporter = None

    def create_exporter(self):
        if self.exporter is None:
            self.exporter = JsonDataExporter()
        return self.exporter


class StrExporterFactoryAbstract(DataExporterFactoryAbstract):
    exporter = None

    def create_exporter(self):
        if self.exporter is None:
            self.exporter = StringDataExporter()
        return self.exporter


type = "json"
[print(de.export(animal)) for animal in animals]
