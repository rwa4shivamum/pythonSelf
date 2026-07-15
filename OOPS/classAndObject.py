class Student:
    name = "Shivam"
    age = 20

#creating Object
s1 = Student()
print(s1.name, s1.age)


#self
class Student:
    def show(self):
        print("Hello WOrld")

s1 = Student()
s1.show()


class Student:
    def setData(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student()

s1.setData("shivam", 20)
s1.show()


#3.contructor , deconstructor
class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor Called")

