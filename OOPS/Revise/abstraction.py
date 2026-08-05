#Abstraction
'''
- Using abstraction, We can hide the implementation part. (In Encap we private the method and attributes)
- we focus on how to hide instead of how to do.

- We can acheive abstraction using:
a. Abtract Class 
b. Abstract Method

ABstract Class:(step to make)
--------------
- A class which can't be instantiated. (object can't be created).
- A abstract class can also contain non-abstract/concrete methods
- An abstract class must have at least one abstract method.
- We can create an abstract class by inherit a class "ABC" from abc module.


Abstract Method:
--------------
- A method without it's body.
- We can create an abstract method by applying a decorator "@abstractmethod" from abc module.


Use Case:
---------
- To enforce some rules which must be satisfied in child classes
'''

from abc import ABC, abstractmethod #this gives from python abc library

class Animal(ABC): #here, ABC class was parent
    
    @abstractmethod #this was the decorator
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print("Dog is barking....")
    pass

class Lion(Animal):
    def sound(self):
        print("Lion is roaring....")
    pass

o = Dog()
o.sound()

o2 = Lion()
o2.sound()



class ReserveBank(ABC):
    
    @abstractmethod
    def roi(self, rate=4.2):
        pass

class Axis(ReserveBank):
    def roi(self, rate=4.2):
        self.roi_value = rate
        
    def display(self):
        print(self.roi_value)
        
class Bob(ReserveBank):
    def roi(self, rate=4.2):
        self.roi_value = rate
        
    def display(self):
        print(self.roi_value)
        
axis_bank = Axis()
axis_bank.roi(8.6)
axis_bank.display()

bob_bank = Bob()
bob_bank.roi()
bob_bank.display()



class Authentication(ABC):
    
    @abstractmethod
    def sign_up(self):
        pass
        
    @abstractmethod
    def sign_in(self):
        pass
    
    @abstractmethod
    def sign_out():
        pass
    
class Theme(ABC):
    
    @abstractmethod
    def light_Theme(self):
        print("light Theme")
    
    @abstractmethod
    def dark_Theme(self):
        print("Dark theme")
        
class MyApp(Authentication, Theme):
    def sign_up(self):
        print("User signed up succesfully.....")
        
    def sign_in(self):
        print("User signed in Succsessfully....")
        
    def sign_out(self):
        print("User signed out Successfully....")
        
    def light_Theme(self):
        print("User changed the Theme to light...")
    
    def dark_Theme(self):
        print("User chenged the Theme to Dark....")

user1 = MyApp()
user1.sign_up()
user1.sign_in()
user1.sign_out()
user1.light_Theme()
user1.dark_Theme()