C = type("C", (), {"__init__": lambda self, x: setattr(self, "var", x), "var": 42})
c = C(123)
print(C.var)
print(c.var)
