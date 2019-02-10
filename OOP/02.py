class A():
    name = "May"
    age = 20

    def say(self):
        self.name = "zym"
        self.age = 21


# 此时，A称为类实例
print(A.name)
print(A.age)
# id可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.name))
print(id(A.age))

print("*" * 20)

a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print(A.__dict__)
print(a.__dict__)

print("*" * 20)
# 修改类实例中的属性
A.name = "mayyzym"
print(A.name)
print(a.name)
print(id(A.name))
print(id(a.name))

print(A.__dict__)
print(a.__dict__)

print("*" * 20)

# 修改对象的属性
a.name = "zym"
print(A.name)
print(a.name)
print(id(A.name))
print(id(a.name))

print(A.__dict__)
print(a.__dict__)
