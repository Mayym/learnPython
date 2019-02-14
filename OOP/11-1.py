# __call__举例
class A():
    def __init__(self):
        print("A")

    def __call__(self):
        print("AA")

    def __str__(self):
        return "AAA"


a = A()
a()
print("-" * 60)


# __str__举例
print(a)
