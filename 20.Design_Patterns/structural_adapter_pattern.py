import json
from structural_decorator_pattern import DataExporter


# Adapter
class JsonDataExporter(DataExporter):
    def export(self, data):
        return json.dumps(data.__dict__)


# Adapter
class StringDataExporter(DataExporter):
    def export(self, data):
        return str(data)
