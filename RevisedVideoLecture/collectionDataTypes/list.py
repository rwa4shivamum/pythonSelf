'''
- A collection of multiple element with same or different data type 
- It is denoted by []
- Indexed value start from 0
- List is mutable
- hetrogenous

List Operation
_____________
a.Indicing
b.Slicing
c.CRUD operation (All operation can be performed)

'''

lstOfDATA = [12,3,3,42,13]
print(lstOfDATA[::-1])#reverse
help([])#this give the how we can use which method

del lstOfDATA[0], lstOfDATA[-1] #this allow to us
del lstOfDATA[0:1]
print(lstOfDATA)