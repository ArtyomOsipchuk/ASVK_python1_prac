import pickle
p = pickle.dumps({"a": 1, "b": 2, "c": 3}, protocol=0)
pp = pickle.loads(p)
print(pp["b"])
