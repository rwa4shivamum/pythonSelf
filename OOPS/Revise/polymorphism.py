'''
Polymorphism
Poly-Multiple
Morphism-behaviour or forms
MUltiple behaviour

Types->
    1.compile-time polymorphism
      -Method overloading
      -operator overloading
    2.Run-time Polymorphism
      -Method overriding
      -
'''
"""
Method overloading-steps
-----------------
   -Single Class
   -Multiple Mehods(not for python)
   -method name must be same, but parameter different
   -For python: Use Single method with Arbitary Argument(*args)
"""
class Vehicle:
    def truck(self, *args):#here *n means it can take either 0 or more than 0 
        if len(args)==0:
            print("truck is empty")
        elif(len(args)==1):
            print(f"Truck runing with: {args[0]} passengers")
        else:
            print(f"Truck is rnunning with {args[0]} passengers")
    
obj = Vehicle()

obj.truck()
obj.truck(10)
obj.truck(10,20,30)


'''
Method overiding
---------------
    -Multiple Class (Inheritance is Required)
    -Multiple Mehods
    -Method name must be same, also parameter are same
    
'''  

class India:
    def wearing(self):
        print("Waering Dhoti Kurta")
    
class Pak(India):
    def waering(self):
        print("Wearing Pathani")

abdullah = Pak();
abdullah.waering()#Wearing Pathani
#but I need both output while calling once how using two ways

class India:
    def wearing(self):
        print("Waering Dhoti Kurta")
    
class Pak(India):
    def waering(self):
        aman = India()#this create another object
        aman.wearing()
        print("Wearing Pathani")
        
abdullah = Pak();
abdullah.waering()#now Waering Dhoti Kurta,
                  #    Waering Patani
#but above solution have one catch it create a 

class India:
    def wearing(self):
        print("Wearing Dhoti Kurta")
        
class Pak(India):
    def wearing(self):
        super().wearing()
        print("Pathani Waering")
        
aman = Pak();
aman.wearing()
