#Function 
'''
-- A block of code that is reusable

Types:
1.Built In Function (System Defined)
2.User Defined Function (UDF)

Built-in Function:
-----------------
- We hve more than 60 built-in Function
function for various opeartion
- For example
print(),
input(),
len(),
type(),
id(),
etc.....


User Defined Function (UDF):
---------------------------
- A function that is made by user.
- We can create UDF by following four ways
1.TNRN
2.TSRN
3.TNRS
4.TSRS

Syntax:
-------
def function_name(parameters):
    body
    return value

'''


#Types of Function Arguments/Parameters
'''
1. Required Positional Argument
2. Optional Argument
   i.Aribitary Arguments
   ii.keyword Arguments
3.Default Argument
'''

'''
Required Positional Arguments
def get_fruits(n1,n2):
    print(n1,n2)

get_fruits("apple","cherry")# Required Positional Argument
get_fruits("apple") #it gives an Error
'''

'''
default argument has not to passed first argument as default if one argument as default
def get_fruits(n1, n2='Kivy'):
    print(n1,n2)
    
get_fruits("apple","cherry")
get_fruits("apple")
'''


#arbitary Argument 
'''data Types of arbituary is tuple
def get_fruits(*args):
    print(args)
    
get_fruits()
get_fruits("apple")
get_fruits("apple", "cherry")
get_fruits("apple","cherry","mango")
'''


#keyWord Arguments
def prepare_pizza(**kwargs):
    print(kwargs)
    
prepare_pizza(cheese=50, tomato=2, olives=5)
prepare_pizza(cheese=10000, tomato=1, olives=15, onion=15, type="cheese burst")


def print(*args, **kwargs):
    pass

print("om")
print("om", "vaja")
print("om", "vaja", end="\n", sep=" ")


# docstrings (document string)
'''
-- A documentation for any objects in Python such as function, class, module, or package.

How to Create a DocString:
-------------------------
- We must have to write a docString as a multi-line string wihtin a class , module, or package.

How to acccess a Docstring:
Using:
    i. __doc__ attibute
    ii. help() function
'''
def addition(a,b):
    '''This function returns an addition of given two number 
    Parameter:
    a:number
    b:number
    
    Return Value:
    -------------
    a+b: number
    '''
    return a+b

print(help(addition))
print(addition.__doc__)
