import inspect

class A:
    a: int

    def __init__(self, var):
        if not isinstance(var, inspect.get_annotations(self.__class__)["a"]):
            raise TypeError("Parametr must be int")
        self.a = var
