class A:
    pass
class B(A):
    pass
class X(B, A):
    pass
class X(A, B):
    pass
