#Set in python
#set is unordered, no duplicates values, mutable collection
# s = {1,2,3,4,2,3,2,1}
# print(s)
# s = {1, 2, 10}
# s.add(3)
# s.remove(2)   # error if not found
# s.discard(1)   # NO error if not found
# print(s)  # {1, 2, 3}

a = {1, 2}
b = {2, 3}
# print(a.union(b))   # {1, 2, 3}


print(a.difference(b))   # {1}


student = {
    "name": "Shivam",
    "age": 20,
    "marks": 90
}

print(student["name"])   # Shivam

print(student.get("age"))      # 20
print(student.get("city"))     # None (safe)

print(student.keys())    # all keys
print(student.values())  # all values
print(student.items())   # (key, value)

student.update({"age": 21})

student.pop("marks")

for k, v in student.items():
    print(k, v)