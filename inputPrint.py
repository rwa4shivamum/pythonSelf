# print("Hello", "world" , sep="-", end="!")

# name = "Shivam"
# age = 20

# print(f"My name is {name} and age is {age}")
# #f-string based

# #print("Hello" + 5)#Error

# print("Hello" + str(4))

# num = input("Enter Number:")
# print(int(num) + 5)

# # name = "2"
# if name.isdigit():
#     name = int(name)
# else:
#     print("Invalid Number")


# x = 10
# name = "shivam"

# #vairable
# x = 10
# name = "shivam"

#dataTypes int, float, str, bool, list, tuple, dict

print(type(2.5))#float
print(type("2"))#string
print(type(2))#int
print(type(True))#bool
print(type([1,2,3]))#list
print(type((1,2,3)))#tuple
print(type({"a":1}))#dictionary


#Arithmetic operator
#+,-,*,/,//,%,**
print(2+4)
print(2-2)
print(2*2)
print(2/2)
print(10//3)
print(10%2)
print(10**2)

#comparision
print(10>1, 20<3, 20!=20, 10==2, 10>=2)

#logical operator
print(10>1 and 10>5)
print(10>2 or 20 < 15)
print(not 10>2)#always toggle the bool
print(-5 // 2)  # -3  ❗ (important))

#type Casting 
print(type(int("10")))
print(type(float("10.5")))
print(type(str(10)))

# int("10.5") erorr 
print(type(int(float("10.5"))))


#implicit type casting
a = 5
b = 2.5

c = a+b
print(c)
print(type(c)) #float converted by python itself

#what is complex in pthon ?
# real part + imaginary part in python
# a + bj
# a=real part b = imaginary part and j= √(-1)

x = 3 + 2j
print(x.real, type(x.real))#3.0 always be in flaot
print(x.imag, type(x.imag))#2.0
print(type(x))#complex

print((2+3j) + (3+3j),"addition")
print((5 + 3j) - (2 + 1j), "subtraction")
print((1 + 2j) * (3 + 4j), "multiplication")
print((1 + 2j) / (1 + 1j), "divide")

#🧠 Summary
# Complex = a + bj
# j = imaginary unit
# Supports math operations
# No comparison allowed
# Use .real & .imag
# Created using complex()
x = 3 + 4j

print(x.real)
print(x.imag)
print(abs(x))
print(x.conjugate())
print(type(x))

#int->float->complex

print(float(2))
print(  )