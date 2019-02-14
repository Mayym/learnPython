# MRO原则

class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
class E(B, C, D):
    pass

print(E.__mro__)