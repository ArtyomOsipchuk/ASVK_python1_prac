class sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
                raise TypeError("Cannot have more tan one parent")
        return super().__new__(metacls, name, parents, namespace)

class E(metaclass=sole): pass
class C: pass
try:
    class A(C, E): pass
except Exception as e:
    print(e)

class B(C, int): pass
