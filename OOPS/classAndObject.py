# class Student:
#     name = "Shivam"
#     age = 20

# #creating Object
# s1 = Student()
# print(s1.name, s1.age)


# #self
# class Student:
#     def show(self):
#         print("Hello WOrld")

# s1 = Student()
# s1.show()


# class Student:
#     def setData(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name, self.age)

# s1 = Student()

# s1.setData("shivam", 20)
# s1.show()


# #3.contructor , deconstructor
# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Constructor Called")


# class Student:
#     def setData(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)

# s1 = Student()
# s1.setData("Shivam")
# s1.show()

class Student:
    name = "default"

s1 = Student()
print(s1.name)

class Student:
    def setName(self,name):
        self.name = name

    def showName(self):
        print(self.name)

s1 = Student()
s1.setName("shivam")
s1.showName()


#constructor
class Student:
    def __init__(self, name):
        self.name = name
        print("Contructor is Called")
    
    def __del__(self):
        print("deconstructer is called")

s1 = Student("Shivam")

#del keyword del keyword to del the varible
num = 12
print(num)
del num
# print("num is deleted", num)#getting error


#7.Encapsulation => data hiding + control access
#Types of varible in python:-publi
# | Type      | Syntax | Access               |
# | --------- | ------ | -------------------- |
# | Public    | name   | Anywhere             |
# | Protected | _name  | Within class & child |
# | Private   | __name | Only inside class    |

class Student:
    def __init__(self, name, age, email):
        self.name = name #public
        self._age = age  #protected _age
        self.__email = email #private __email
    def show(self):
        print(self.name, self._age, self.__email, "Here from private,public, protected")
    def __del__(self):
        print("calling dtor")


s3 = Student("shivam", 23, "gam.coom")
# print(s3.__email) this get error b'cuz it is private
s3.show()

# ✔ Class → Blueprint
# ✔ Object → Instance
# ✔ self → current object
# ✔ init → constructor
# ✔ del → destructor
# ✔ del → delete object/variable
# ✔ Encapsulation → data protection

class BankAccount:
    def __init__(self,name):
        self.name = name
        self.__balance = 0

    def withdraw(self,amount):
        if(amount <= self.__balance):
            self.__balance -= amount
            return True,amount
        else:
            return False,"not withdraw"
        
    def deposit(self,amount):
        self.__balance += amount
        return True,"balance added Successfully"
    
    def showBalance(self):
        return self.__balance
    
b1 = BankAccount("shivam")
print(b1.deposit(2000))
print(b1.showBalance())
print(b1.withdraw(500))
print(b1.showBalance())