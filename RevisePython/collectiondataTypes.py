# collection data types
#str, list, tuple, set, dict(dictionary)
string = "Helo World"
conbined = string  + "Shivam"
print(conbined)
#repeat stringusing * operator
strging2 = "sehi" * 3
print(strging2)
#3.indexing
print(strging2[0])
print(strging2[-1])
#4.slicing
print(strging2[1:4])
#5.length of string
print(len(strging2))

#string methods
str  = "   HEllokj world "
print(str.lower())
print(str.upper())
print(str.title())
print(str.capitalize())
print(str.strip())

# print(str.split())
# print(str.join())
print(str.find("World"))
print(str.replace("world", "Python"))

#string fomatting
name = "Shivam"
age = 21
print(f"I am {name} and my age {age}")


#list donating like this [] and also this was the 
lstOfDatatpyes = [1,"shivam",True,2.5]
for i in lstOfDatatpyes:
    print(i)

# characteristics
#Ordered: The items in a list have a specific order, and that order is maintained. Each item can be accessed using its index, where indexing starts from 0.
#mutable(can Change)
#heterogenrous
#dynamic(data allocation)

# del lstOfDatatpyes
# print(lstOfDatatpyes) getting error not defined

lstOfDatatpyes.remove(1)
# Create a list
my_list = ['apple', 'banana', 'cherry', 'banana']

# Remove the first occurrence of 'banana'
my_list.remove('banana')
print(my_list)  # Output: ['apple', 'cherry', 'banana']

# Trying to remove an element that does not exist will raise an error
# my_list.remove('grape')  # Uncommenting this will raise ValueError

#pop remove last element

#method of list
# mylist = [1,2,3]
# mylist.append(4)
# mylist.extend([6,7])# my_list.extend(another_list)
# mylist.insert(1,4)# my_list.insert(index, value)
# my_list.remove(2)# my_list.remove(value)
# popped_item = my_list.pop()
# print(popped_item)  # Output: 3
# print(my_list)      # Output: [1, 2]
# index_of_20 = my_list.index(20)
# count_of_20 = my_list.count(20)
# copied_list = my_list.copy() # copied_list is [10, 20, 30]
# my_list.clear()
# my_list.pop()


"""--------------------------------Tuple----------------------------------
1.orderd
2.immutable
3.Hetrogenous
4.indexing and slicing
5. nested tuple
6. memory efficient
"""

# Creating a tuple
my_tuple = (1, 2, 3, "hello", 4.5)
# Slicing the tuple
subset = my_tuple[1:4]  # Output: (2, 3, "hello")
#my_tuple[3] = "world" #tuple is immputable
print(my_tuple)
# del  my_tuple

#method of tuple
print(my_tuple.count(1))
print(my_tuple.index('hello'))

"""___________________________SET__________________________________________
1.unordered: The elements in a set do not have a defined order, and you cannot access them using indexes.
2.unique ELement
4.mutable
4.dynamic size
"""
my_set = {1,2,3,4}
my_set.add(5)
my_set.update([6,7])
print(my_set)
another_set = set([3,4,4,5,6])
print(another_set)

print(4 in another_set)

# Define a set
my_set = {1, 2, 3, 4, 5}

# Removes a specified element from the set.
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

# Attempting to remove a non-existing element
my_set.remove(10)  # Raises KeyError

# Removes a specified element from the set.
my_set.discard(4)
print(my_set)  # Output: {1, 2, 5}

# Attempting to discard a non-existing element
my_set.discard(10)  # No error

# Remove and return an arbitrary element
removed_element = my_set.pop()
print(removed_element)  # Output: 1 (or any other element, as the order is arbitrary)
print(my_set)  # Output: Remaining elements in the set

# Attempting to pop from an empty set
empty_set = set()
empty_set.pop()  # Raises KeyError

# Clear the set
my_set.clear()
print(my_set)  # Output: set()


#method of set
#add()

my_set = {1,2,3}
my_set.add(4)
print(my_set)

my_set.remove(2)
my_set.discard(2)
my_set.pop()
my_set.clear()
my2nd_set = {1,2,3,6,7,8}
result = my_set.union(my2nd_set)
print(result)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3} 