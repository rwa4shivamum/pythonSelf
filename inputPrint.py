# # print("Hello", "world" , sep="-", end="!")

# # name = "Shivam"
# # age = 20

# # print(f"My name is {name} and age is {age}")
# # #f-string based

# # #print("Hello" + 5)#Error

# # print("Hello" + str(4))

# # num = input("Enter Number:")
# # print(int(num) + 5)

# # # name = "2"
# # if name.isdigit():
# #     name = int(name)
# # else:
# #     print("Invalid Number")


# # x = 10
# # name = "shivam"

# # #vairable
# # x = 10
# # name = "shivam"

# #dataTypes int, float, str, bool, list, tuple, dict

# print(type(2.5))#float
# print(type("2"))#string
# print(type(2))#int
# print(type(True))#bool
# print(type([1,2,3]))#list
# print(type((1,2,3)))#tuple
# print(type({"a":1}))#dictionary


# #Arithmetic operator
# #+,-,*,/,//,%,**
# print(2+4)
# print(2-2)
# print(2*2)
# print(2/2)
# print(10//3)
# print(10%2)
# print(10**2)

# #comparision
# print(10>1, 20<3, 20!=20, 10==2, 10>=2)

# #logical operator
# print(10>1 and 10>5)
# print(10>2 or 20 < 15)
# print(not 10>2)#always toggle the bool
# print(-5 // 2)  # -3  ❗ (important))

# #type Casting 
# print(type(int("10")))
# print(type(float("10.5")))
# print(type(str(10)))

# # int("10.5") erorr 
# print(type(int(float("10.5"))))


# #implicit type casting
# a = 5
# b = 2.5

# c = a+b
# print(c)
# print(type(c)) #float converted by python itself

# #what is complex in pthon ?
# # real part + imaginary part in python
# # a + bj
# # a=real part b = imaginary part and j= √(-1)

# x = 3 + 2j
# print(x.real, type(x.real))#3.0 always be in flaot
# print(x.imag, type(x.imag))#2.0
# print(type(x))#complex

# print((2+3j) + (3+3j),"addition")
# print((5 + 3j) - (2 + 1j), "subtraction")
# print((1 + 2j) * (3 + 4j), "multiplication")
# print((1 + 2j) / (1 + 1j), "divide")

# #🧠 Summary
# # Complex = a + bj
# # j = imaginary unit
# # Supports math operations
# # No comparison allowed
# # Use .real & .imag
# # Created using complex()
# x = 3 + 4j

# print(x.real)
# print(x.imag)
# print(abs(x))
# print(x.conjugate())
# print(type(x))

# #int->float->complex

# print(float(2))

# #bool conversion
# #True = 1 and false = 0
# print(int(True))
# print(int(False))

# print(float(True))
# print(float(False))

# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool(""))
# print(bool("Hello"))
# print(bool([]))

# bool([1,2])

# print(int(float("10.5")))

# | From \ To | int | float | bool | str |
# | --------- | --- | ----- | ---- | --- |
# | int       | ✔️  | ✔️    | ✔️   | ✔️  |
# | float     | ✔️  | ✔️    | ✔️   | ✔️  |
# | bool      | ✔️  | ✔️    | ✔️   | ✔️  |
# | str       | ⚠️  | ⚠️    | ✔️   | ✔️  |
# ⚠️ = Only if valid format

x = 10
#print(id(x))

# # a = 10
# # b = 10

# a = 100000000000
# b = 100000000000

# print(id(a), id(b))

# x = [1,2]
# y = x

# y.append(3)

# print(x)  # [1,2,3]
# print(10 + int("5"))   # Try breaking

# print("10","20", "30", sep="-")

# name = input("Enter your name:")
# print("Hello", name)
# a=float(input("Enter num1:"))
# b=int(input("Enter num2:"))

# print(a*b)

# a=bool(input("Enter numbe:"))
# print(type(a),a)

# print(type("10"))
# print(type(10))
# print(type(10.0))
# print(int("123"))
# print(str(50))
# print(int(10.9))
# print(int("abc"))#error write a valid number
# print(float("10a"))#ValueError: could not convert string to float: '10a

# print(int(float("10.5")))

# print(list("hello"))#['h', 'e', 'l', 'l', 'o']
# print(set("hello"))#{'o', 'e', 'l', 'h'}

# print(int("1000"))
# print(float("100.5"))
# print(str(100))
# print(tuple([1,2,3]))
# print(list((1,2,3)))

a = 10
b = 10
# print(id(a), id(b))

# ab = 100000000000000000000000000000000000000033333222223222333222222222222
# bv = 100000000000000000000000000000000000000033333222223222333222222222222

# print(id(ab), id(bv))

a = "10"
b = 5
print("%" * 3)#here mutiple of this modulo
print(a + str(b) * 3)