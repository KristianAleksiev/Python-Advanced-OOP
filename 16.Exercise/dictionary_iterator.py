class dictionary_iter:
    def __init__(self, dict_obj):
        self.items = list(dict_obj.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        result_to_return = self.items[self.index]
        self.index += 1
        return result_to_return


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
