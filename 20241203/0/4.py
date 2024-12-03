class Doubleton(type):
    _instance = []
    _counter = 1
    def __call__(cls, *args, **kw):
        if len(cls._instance) < 2:
            cls._instance.append(super().__call__(*args, **kw))
        cls._counter = (cls._counter + 1) % 2
        return cls._instance[cls._counter]

class S(metaclass=Doubleton):
    A = 3

s, t = S(), S()
ss, tt = S(), S()
s.newfield = 100500
tt.newfield = 42
print(f"{s.newfield=}, {t.newfield=} {ss.newfield=}, {tt.newfield=}")
print(f"{s}, {t} {ss}, {tt}")
print(f"{s is t=}")
