def fun(a: int, b: float=1.23) -> float:
    return a * b

print(fun("rRrraRhrsR", 3))
print(fun.__annotations__)

import inspect
print(inspect.get_annotations(fun))

from future import annotations
print(fun.__annotations__)

class C:
    a: int = 100500
    b: float

print(C.a)
print(C.b)
