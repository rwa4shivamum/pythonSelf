# #Inheritance means getting properties of parents to child like child inherit the property of child

# #Types of inheriatnce
# #1.Single level Inheritance
# class Animal:
#     def speak(self):
#         print("Animal Speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
    
# d = Dog()
# d.speak()
# d.bark()

# #2.Multiple Inheritance One child-> multiple parents like mom and dad
# class Father:
#     def __init__(self,Fathername):
#         self.Fathername = Fathername
#     def skill1(self):
#         print("driving Skill")

# class Mother:
#     def __init__(self, Mothername):
#         self.Mothername = Mothername

# class Child(Father, Mother):
#     def __init__(self,name, Fathername,Mothername):
#         Father.__init__(self, Fathername)#calling both parent
#         Mother.__init__(self,Mothername)
#         self.name = name

#     def fullName(self):
#         print(self.Fathername,self.Mothername, self.name)

# s1 = Child("shivan", "manmohan", "rahsi")
# s1.fullName()

# # 3.Multilevel Inheritance
# class A:
#     def showA(self):
#         print("A")
    
# class B(A):
#     def showB(self):
#         print("B")
    
# class C(B):
#     def showC(self):
#         print(C)
    
# obj = C()
# obj.showA()
# obj.showB()
# obj.showC()


# #4. Hierarchical Inheritance
# #one parent -> multiple children

# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# Dog().eat()
# Cat().eat()

# #5. Hybrid Inheritance-combination of multiple types


# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B,C):
#     pass

# #Important Concept: MRO (Method Resolution Order)

# #👉 Python decides which method to call first
# print(D.mro())



# # 🔷 2. Reflection Enabling Functions

# # 👉 Reflection = introspection
# # 👉 Means: Python can inspect objects at runtime
# x = 10
# print(type(x))
# print(x.__and__(2))
# print(x.bit_count())
# print(id(x))

# # dir 👉 Shows all properties & methods
# print(dir(x))

# m = [1,2,3,4]
# print(dir(m))

# class Student:
#     name = "Shivam"

# s = Student()
# print(getattr(s, "name"))

# # 5. setattr()

# # 👉 Set value dynamically

# setattr(s, "age", 20)
# print(s.age)

# # 6. hasattr()
# # 👉 Check attribute exists

# print(hasattr(s, "name"))  # True

# # 7. delattr()
# # 👉 Delete attribute

# delattr(s, "name")


#3.Nested Function
def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()

#closure
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(10))
print(add5(20))

# 🔷 Final Summary

# ✔ Inheritance → reuse code
# ✔ Types → Single, Multiple, Multilevel, Hierarchical, Hybrid
# ✔ Reflection → inspect & modify objects dynamically
# ✔ Nested function → function inside function
# ✔ Closure → remembers outer variables