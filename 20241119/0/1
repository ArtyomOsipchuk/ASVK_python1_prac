class C:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        """I'm the 'x' property."""
        if self._age == 42:
            print("secret value!")
            return -1
        return self._age

    @age.setter
    def age(self, value):
        if value > 128:
            raise ValueError
        self._age = value

    #@age.deleter
    #def age(self):
    #    del self._age

c = C()
c.age = 127
c.age = 42
print(c.age)
c.age = 129
