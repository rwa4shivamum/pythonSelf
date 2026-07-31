# Dictionary
"""
-- A collection of multiple element in the form of key-value pairs
-- It is denoted by {}
-- Dictionary is mutable
-- Each key must be unique

Dictionary OPerations:
-------------------
a.Indexing
b.Slicing
c.CRUD operation (All operation possible)

"""

d = {"id": 123, "name": "Dhruv"}
d["age"] = 23  # this make a new key:value pair
d["name"] = "Vivek"
d.pop("name")  # delete the item as per key
d.popitem()  # latest key:value pair remove

del d["id"]  # allowed in dictionary or where indexing is available
print(d)

d = {"id": 101, "name": "dhruv", "age": 22}

for i in d:
    print(i)

for i in d.keys():
    print(i)  # o/p tuple

for i in d.values():
    print(i)  # o/p tuple

for i in d.items():
    print(i)  # o/p tuple

t = (12, 56, 89)
a, b, c = t  # tuple unpacking
print(a, b, c)
l = [12, 14, 15]
a, b, c = l
print(a, b, c)

a = 10
b = 20

a, b = b, a  # this was swapping the tuple
print(a)
print(b)

for k, v in d.items():
    print(f"{k}+==>>> {v}")


# type Casting Constructor
"""
1.list()
2.tuple()
3.set()
4.frozenset()
5.dict()
"""

l = ["a", "b", "c"]
tuple(l)

l1 = [12, 12, 13, 14, 15, 15, 15, 16, 16, 17, 18]
l2 = set(l1)
print(list(l2))

print(frozenset(l))

# print(dict(l1)) #getting error due to it required key:value pair

data = [("A", "Apple"), ("B", "Banana"), ("C", "Cherry")]
# list of tuple
print(dict(data))

# to create a Dictionary
# 1. list of tuple
# 2. tuple of list
# 3.list of list
# 4.tuple of tuple

for i in range(5):
    print("hello")
    print("ehllo")
