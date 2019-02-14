# 元类演示
# 元类写法是固定的，它必须继承自type，元类一般命名以MetaClass结尾
class SchoolMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("元类")
        attrs['id'] = '000'
        attrs['addr'] = 'ABC'
        return type.__new__(cls, name, bases, attrs)

# 元类定义完就可以用，使用时注意写法
class Teacher(object, metaclass=SchoolMetaClass):
    pass


t = Teacher()
print(t.id)
