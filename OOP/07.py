# Mixin案例
class Person():
    name = "May"
    age = 18

    def eat(self):
        print("EAT")

    def drink(self):
        print("DRINK")

    def sleep(self):
        print("SLEEP")


class Teacher(Person):
    def work(self):
        print("Work")


class Student(Person):
    def study(self):
        print("Study")


class Tutor(Teacher, Student):
    pass


t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)
print("-" * 100)


class TeacherMixin():
    def work(self):
        print("Work")


class StudentMixin():
    def study(self):
        print("Study")


class TutorM(Person, TeacherMixin, StudentMixin):
    pass


tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
