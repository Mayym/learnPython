# __getattr__
class A():
    name = "NoName"
    age = 18

    def __getattr__(self, attr_name):
        print("A")
        print(attr_name)


a = A()
print(a.addr)
print("-" * 60)

# __setattr__
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性： {0}\n"
              "设置其值： {1}".format(name, value))
        # 该语句导致死循环：self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name, value)


p = Person()
print(Person.__dict__)
p.age = 18
