#  SINGLETON PATTERN

class MyClass:
    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise TypeError("Singletons cannot be created with init")

    @classmethod
    @property
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = MyClass()
        return cls.__instance


mc1 = MyClass.instance
mc2 = MyClass.instance
print(mc1 == mc2)
print(mc1)
print(mc2)


#  With decorator

def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


@singleton
class MyClass2:
    pass


mc3 = MyClass2()
mc4 = MyClass2()
print(mc3 == mc4)
print(mc3)
print(mc4)
