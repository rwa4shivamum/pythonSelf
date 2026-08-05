#Poly Morphism
'''
Multiple forms 
like: a girl: sister, mother, daughter, wife
like: a boy:(launda) 
Two-types: 
   1.compile time
   2.runtime 

1.compile-Time
   i.method overloading(truck overloading)
   ii.method overrding
   
Method overloading (steps)
- single class
- Multiple methods
- methods name must be same, but parameters differnct
- arbitary args
'''

class Vehicle:
    def truck(self):
        print("truk empty")
    
    def truck(self,a):
        print("truck full")
        
    def truck(self,a , b):
        print("truck, was overloaded")

#this above was the method overloadind examplem, but this works all other langauge except python we have arbitary arugument in it

class Vehicle:
    def truck(self,*args):
        if(len(args)==0):
            print("truck is empty")
        elif(len(args)==1):
            print("truck is loaded")
        else:
            print(f"truck is overlaoded {[i for i in args]}")

truck1 = Vehicle()
truck1.truck()
truck1.truck(10)
truck1.truck(10,20,30,40,50)


'''
Method Overriding 
------------------
    - Multiple Classes (inheritance is required)
    - Multiple methods
    - Methods name must be same, also parameter are same
    - by accessing parents class element we used super() keywords
'''
class India:
    def wearing(self):
        print("Dhoti Kurta")
        

class Pak(India):
    def wearing(self):
        print("Pathani-Kurta")
    
obj = Pak()

obj.wearing()


#

class India:
    def wearing(self):
        print("Dhoti-Kurta")
    
class Pak(India):
    def waering(self):
        dummy = India() #but here we create an object again
        dummy.wearing()
        print("Pathani-Kurta")
 
 
       
class India:
    def wearing(self):
        print("Dhoti-Kurta")
    
class Pak(India):
    def waering(self):
        super().wearing()
        print("Pathani-Kurta")
        
aman = Pak()
aman.waering()




class India:
    def wearing(self):
        print("Dhoti-Kurta")
    
class Iran:
    def wearing(self):
        print("Burkha")
        
class Pak(Iran, India):
    def waering(self):
        super().wearing()
        print("Pathani-Kurta")
        
aman = Pak()
aman.waering()

#where ploymorphism, and where method overiding, method overloading used, 
print(issubclass(Pak,India))