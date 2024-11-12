class A:
    __v = 0 # => в dir будет _A__v

    def inc(self):
        self.__v += 1
        print(self.__v)

class B(A):
    __v = 100500 # => в dir будет _B__v


b = B()
b.inc()
b.inc()
b.v = 42
b.inc()
print(B._A__v)
