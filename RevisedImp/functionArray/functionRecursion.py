# def main():
#     print("Hello")
#     main()
    
# main()

#WAP to find function recursion
#!5 = 5*4*3*2*1
input = 5
result = 1
for i in range(input,0,-1):
    result *= i
    
print(result)

def factorial(n):
    if(n==1):
        return 1
    
    return n*factorial(n-1)

print(factorial(5))


#Anonymous / lambda function
'''
-- A function without a name is called anonymous function
-- This function does'nt have a multi-line body
-- This function must return some value or expression.

Syntax:
------
lambda arguments: expression

summation = lambda a, b: a+b

'''

def add(a,b):
    return a + b
addition = lambda a,b: a+b
print(addition(4,5))
summation = lambda _: "banana"

print(summation('hello'))


#Global Keyword
'''
-- Using global keyword we can access global variable inside a local scope.
'''

x = 5

def disp():
    global x
    x = 7 #not new variable make as x it goes update the value of x varibale as 7 beacuse internal we defined it global 
    print(x)
    
print(x)#here before calling the function disp which was make x as global variable so, it won't update after calling dsip() it got updated
disp()
print(x)
