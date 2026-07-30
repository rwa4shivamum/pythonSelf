#string Formatting / String Interpolation
a = 4
b = 5
c = a+b
print("sum of a and b is ", a + b)

print("Sum of %d and %d is %d" %(a,b,c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {om} and {devan} is {meet}".format(om=a, devan=b,meet=c))

print(f"sum of {a} and {b} is {c}")#formatted string
print("DHRUV".center(10))
print("DHRUV".center(10,"*"))


#Template



#String Manipulation
'''
Q. String Mutability
A. String is not Manipulated
A. String is immutable
'''

s = "Dhruv"
print(s[0])
print(s[1])

#String Operation
'''
a.Indexing
b.slicing
c.CRUD operation
    C - Create
    R - Read
    U - Update 
    D - Delete
'''

print(s[-1])

#slicing
'''
slicing
string[start:end:step]

'''
char = "shivamMishra"
print(char[0:-1:2])
print(char[0:len(char):1])
print(char[::-1])#reverse

s = "shivam"

# update not possible
#s[0] = 'k' #not possible

#delete also not possible
# del char[3] #this not possible
# del char #this was deleting the char permanently


