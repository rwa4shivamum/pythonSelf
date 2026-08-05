class Person():
    def __init__(self):
        self.name = input("Enter a name: ")
        self.age = int(input("Enter a age: "))
        
    def __str__(self):
        return f'Person created with name: {self.name} and age: {self.age}'
    def __del__(self):
        pass
    

class Employee():
    
    def __init__(self,salary=0):
        self._id = int(input("Enter Employee ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.__salary = float(input("Enter a salary: ")) or salary
    
    def getSalary(self):
        return self.__salary
    
    def getID(self):
        return self._id
    
    def setValue(self,salary):
        if(salary < 0):
            return "invalid input"
        else:
            self.__salary = salary
    
    def __str__(self):
        return f"Employee Id {self._id} and Name: {self.name} and age:{self.age} and salary: {self.__salary}"
    def __gt__(self, other):
        return self.getSalary() > other.getSalary()
    
    def __eq__(self,other):
        return self.getSalary() == other.getSalary()
    
    def __lt__(self, other):
        return self.getSalary() < other.getSalary()
        
    def __del__(self):
        pass
    
class Manager(Employee):
    
    def __init__(self):
        super().__init__()
        self.department = input("Enter a department: ")
    
    def __str__(self):
        return f" {super().__str__()} deparment: {self.department}"
    
class Developer(Employee):
    
    def __init__(self):
        super().__init__()
        self.programmingLang =  input("Enter a single Programming langague: ")
        
    def __str__(self):
        return f" {super().__str__()} and ProgrammingLangague {self.programmingLang}"  
    
people = []
while True:
    print('''
          Project OOP Project: Employee Management System
          
          Choose an Operation:
          1.Create a Person 
          2.Create an Employee
          3.Create a manager
          4.Create a Developer
          5.show a Details
          6.Compare Salaries
          7.Exit''')
    inputChoice = int(input("Enter your Choice: "))
    match inputChoice:
        case 1:
            
            p1 = Person()
            people.append(p1)
            print(p1)
        case 2:
            emp1 = Employee()
            people.append(emp1)
        case 3:
            mngr1 = Manager()
            people.append(mngr1)
            print(mngr1)
        case 4:
            dev1 = Developer()
            people.append(dev1)
            print(dev1)
        case 5:
            print('''
                  Choose details to Show:
                  1. Person
                  2. Employee
                  3. Manger
                  ''')
            enterChoice = int(input("Enter your choice: "))
            if enterChoice==1:
                print(p1)
            elif enterChoice==2:
                print(emp1)
            elif enterChoice==3:
                print(mngr1)  
        case 6:
            print('Choose two employees to compare salaries')
            empId1 = input("Enter the first employee's ID (e.g.,121): ")
            empId2 = input("Enter the second employee's ID (e.g., 456: )")    
            
            empA = None
            empB = None
            for i in people:
                if isinstance(i, Employee):
                    if i.getID() == empId1:
                        empA = i
                    elif i.getID == empId2:
                        empB = i
            if empA and empB:
                if empA > empB:
                    print("Employee 1 has higher salary")
                elif empA < empB:
                    print("Employee 2 has higher salary")
                else:
                    print("Both have equal salary")
            else:
                print("Employee is Not found")
        case 7:
            break