#Dictionary
'''
-- A collection of multiple element in the form of key-value pairs
-- It is denoted by {}
-- Dictionary is mutable
-- Each key must be unique

Dictionary OPerations:
-------------------
a.Indexing
b.Slicing
c.CRUD operation (All operation possible)

'''

d = {'id':123, 'name':'Dhruv'}
d['age'] = 23 #this make a new key:value pair
d['name'] = 'Vivek'
d.pop('name') #delete the item as per key
d.popitem() #latest key:value pair remove

del d['id'] #allowed in dictionary or where indexing is available
print(d)

