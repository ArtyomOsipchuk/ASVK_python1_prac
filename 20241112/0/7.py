class A:
    def __str__(self):
        return f"A"

class B(A):
    def __str__(self):
        st = f"{super().__str__()}"
        return st + ":B"

class C(B):
    def __str__(self):
        st = f"{super().__str__()}"
        return st + ":C"

print(A())
print(B())
print(C())
