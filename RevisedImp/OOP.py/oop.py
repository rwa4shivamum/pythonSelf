#Object Oreinted Programming
'''
-- It is programming paradigm in which everytinh is centerd ot object
-- It is new approach of way of coding which is oriented to an object.


Procedural Oreinted Programming(POP)
--------------
Procedure: Function

Object Oreinted Programming (OOP)
-------------
Object: Instance of Class

C lang -> POP
c++ => POP + OOP
python -> OOP + POP



Priciple of OOP
--------------
1.Encapsulation
2.Inheritance
3.Polymorphism
4.Abstraction


Pre-Requirement: Class & Object

Class:
- A bluePrint Of an Object

Object:
- A Instance of Class


Syntax of Class:
calss Class_name:
   attributes
   method
   constructors
   destructor
   
Syntax of Object:
obj_name = Class_name
'''

class Car :
    _compName = None
    _model = None
    _color = None
    _year = None
    
    def setData(self, c, m, cl, y):
        self._compName = c
        self._model = m
        self._color = cl
        self._year = y
            
    def getData(self):
        print(f"{self._compName}, Model: {self._model} , Color: {self._color} , Year: {self._year}")
        
    
    
        


# Name Mangling

car1 = Car()
car2 = Car()
car1.setData("Tata", "Sierra", "yellow", 2026)
car2.setData("Suzuki", "Victoris", "White", 2026)

car1.getData()
car2.getData()



# print(f"Company: {car1.model}, Model: {car1.model}, Color:{car1.color}")


#Encapsulation

'''
Encapsultion is principle of OOP that restricts access to object's data and allows modifications only through methods.
##Protects data form unintended modification
## Uses Private Attributes getter/setter methods to constroll access

Private Attributes
public methods
Setter(to initialize class attributes) and Getter(to get or retrive class attributes)
Self 
'''

class Car :
    _compName = None
    _model = None
    _color = None
    _year = None
    
    def setData(self, c, m, cl, y):
        self._compName = input("Enter the Car Company Name")
        self._model = input("Enter a Car company Model")
        self._color = input("Enter a Car company Color")
        self._year = int(input("Enter a Car company year"))
            
    def getData(self):
        print(f"{self._compName}, Model: {self._model} , Color: {self._color} , Year: {self._year}")
        
    
    
        


# Name Mangling

car1 = Car()
car2 = Car()
car1.setData("Tata", "Sierra", "yellow", 2026)
car2.setData("Suzuki", "Victoris", "White", 2026)

car1.getData()
car2.getData()




#Contructor
'''
- A block of code which is automatically invoked when calss is intiated
- To Careate a contructor we must create dunder init method
- We use a contructor to initialize class attributes, same like a setter
'''

class Car :
    #default Consrtuctor
    def __init__(self):
        self._compName = input("Enter the Car Company Name")
        self._model = input("Enter a Car company Model")
        self._color = input("Enter a Car company Color")
        self._year = int(input("Enter a Car company year"))
    
    #parameterized constructor
    def __init__(self,c,m,cl,y):
        self._compName = c
        self._model = m
        self._color = cl
        self._year = y
        
    def getData(self):
        print(f"{self._compName}, Model: {self._model} , Color: {self._color} , Year: {self._year}")
        
    
    
        


# Name Mangling

#car1 = Car()
#car2 = Car()#this was empty so, called default constructor
car3 = Car("Tata", "Sierra", "yellow", 2026)#this was parameterized constructor
# car1.setData("Tata", "Sierra", "yellow", 2026) #full control b'cuz constructor automatically get called
# car2.setData("Suzuki", "Victoris", "White", 2026)

# car1.getData()
# car2.getData()


'''
Types of Contructors
1.Default Constructor(comp_name = "maruti" )
2.Parameterized Constructor (comp_name)
'''
open("/Users/Project/pythonSelf/pythonSelf/RevisedImp/OOP.py/open.txt", "r")