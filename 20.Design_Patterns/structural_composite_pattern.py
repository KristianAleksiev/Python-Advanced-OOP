import abc


class UiComponent(abc.ABC):
    def __init__(self, identifier):
        self.identifier = identifier

    @abc.abstractmethod
    def get_representation(self):
        pass

    def __str__(self):
        return self.get_representation()


class Heading(UiComponent):
    def __init__(self, identifier, text):
        super().__init__(identifier)
        self.text = text

    def get_representation(self):
        return f"*{self.text}*"


class Button(UiComponent):
    def __init__(self, identifier, text, func):
        super().__init__(identifier)
        self.text = text
        self.func = func

    def click(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def get_representation(self):
        return f"[{self.text}]"


class Text(UiComponent):
    def __init__(self, identifier, text):
        super().__init__(identifier)
        self.text = text

    def get_representation(self):
        return f"*{self.text}*"


"""We could have a component which have components (container)"""


class Container(UiComponent):
    def __init__(self, identifier, children=None):
        super().__init__(identifier)
        if children is None:
            children = []
        self.children = children

    def get_representation(self):
        return "".join(c.get_representation() for c in self.children)


print(Heading("Heading-1", "It works!"))
print(
    Container(
        'container-1',
        [
            Heading("h1", "it works!"),
            Button("btn-1", "Click me", None),


        ]
    )
)