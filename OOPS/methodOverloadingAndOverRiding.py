class Math:
    def add(self,a,b=0,c=0):
        return a + b + c
    
obj = Math()

print(obj.add(1,2))
print(obj.add(1,2,3))

class Math:
    def add(self, *nums):
        return sum(nums)
    
obj = Math()

print(obj.add(1,2))
print(obj.add(1,2,3,4,5))

# 🧠 Key Point:

# 👉 Python mimics overloading, it doesn’t support it directly.


#method overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

d=Dog()
d.sound()
# 🧠 Key Point:
# 👉 Child class overrides parent behavior


#3.subclass
class A:pass
class B(A):pass

print(issubclass(B,A))#true
print(issubclass(A,B))#false

#🔹 4. super()
# 📌 Concept:
# Call parent class methods/constructor

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
    
c = Child()

# DUnder method
# | Method     | Purpose               |
# | ---------- | --------------------- |
# | `__init__` | Constructor           |
# | `__str__`  | String representation |
# | `__len__`  | Length                |
# | `__add__`  | + operator            |
# | `__eq__`   | == comparison         |


# 6. Operator Overloading
# 📌 Concept:

# Change behavior of operators for objects.

# 👉 Achieved using dunder methods
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)  # calls __add__


# | Concept              | Idea                                                 |
# | -------------------- | ---------------------------------------------------- |
# | Overloading          | Same method, different behavior (Python uses tricks) |
# | Overriding           | Child replaces parent method                         |
# | issubclass           | Checks inheritance                                   |
# | super()              | Calls parent method                                  |
# | Dunder methods       | Control object behavior                              |
# | Operator overloading | Customize operators   