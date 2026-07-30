#Set 
'''
A collection of unique element
-It is denoted by {}
-Set is mutable
-This stores all elements

SET Operations:
______
a.Indexing not
b.Slicing not
c.CRUD OPerations(All CRUD operation done here)(We cannot edit or change individual element)
e.Math's Set Operation
1.Union
2.Itersection
3.Difference
4.Symmetric differnce
'''
'''
s = {4,3,5,7,6,9,1,4,3,2}#random order
print(s)

#insert the element
s.add(90)

s2={1,2,3}
s.update(s2)

s.pop()#it remove the first element

print(s)

s.pop()
print(s)

del s
'''

'''
union->get both element of set 
intersection -> get common element on both set
differnce -> get only element in first set
symmetricDifference -> get elemnt which are not common on both element
'''

s1 = {1,2,3,4}
s2 = {3,4,5,6,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))


#frozenSet
'''
a.Indexing
b.Slicing
c.CRUD operations(only Create and Read)
e.Math's Set Operation
1.Union
2.Itersection
3.Difference
4.Symmetric differnce

'''

fs = frozenset({34,56,89,23})
print(fs)
print(dir(fs))