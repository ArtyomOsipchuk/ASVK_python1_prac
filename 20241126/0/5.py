import pickle
class C:
    def __init__(self, ls, dc, num, st) -> None:
        self.ls = ls        
        self.dc = dc
        self.num = num        
        self.st = st

c = C([1, 2, 3], {"a": 1, "b": 2, "c": 3}, 100500, "Hello world!")
pickled = pickle.dumps(c, protocol=0)
del c
unpickled = pickle.loads(pickled)
print(unpickled.__dict__)
