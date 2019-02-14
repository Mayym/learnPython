# issubclass
class A():
    pass

class B(A):
    pass

class C():
    pass


print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(C, object))
print("-" * 60)

# isinstance
a = A()
b = B()
c = C()

print(isinstance(a, A))
print(isinstance(b, A))
print(isinstance(c, A))
print("-" * 60)

# hasattr
class D():
    name = "May"

d = D()
print(hasattr(d, "name"))
print(hasattr(d, "age"))
print("-" * 60)


# dir
print(dir(A))
a = A()
print(dir(a))
