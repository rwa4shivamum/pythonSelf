
# 🧠 Data Types = Ways to Store Data
# String → text
# List → ordered, mutable collection
# Tuple → ordered, immutable collection

# 👉 Golden Rule:

# If data needs to change → use List
# If data must stay fixed → use Tuple

name  = "shivam"
print(name[0])#here positive or normal index
print(name[-1])#here negative index
print(name[0:4])#here slicing

#3. string formatting
name = "shivam"
print("Hello %s" % name)#old style
print("Hello {}".format(name))
print(f"hello {name}")#best way formating

#3. String methods

s = "   hello  world"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.strip())#this remove forward and backword space
print(s.replace("hello", "shivma"))
s.split() 

# Part2-list 
# can mutable, and stores multiple values
lst = [1,2,3,34,4,5]

#imp methods
lst.append(5)
lst.insert(1,10)
lst.remove(2)
lst.pop()
lst.sort()
lst.reverse()

#tuple:- ordered, immutable collection

t = (1,2,3)
#t[0] = 5 #not possible means not add at another position
#where to used: fixed data, safer then list, faster than list

# | Feature  | List    | Tuple      |
# | -------- | ------- | ---------- |
# | Mutable  | ✅ Yes   | ❌ No       |
# | Syntax   | []      | ()         |
# | Speed    | Slower  | Faster     |
# | Use case | Dynamic | Fixed data |

str = "123"
rvstr = ""
#                  3-1=2, >-1,-1                
for i in range(len(str)-1,-1,-1):
    rvstr += str[i]
    
print(rvstr)

str = "skjdfnksnfdweioruwer"

count = 0

for i in str:
    if(i == "a" or i == "e" or i == "i"):
        count += 1

print(count)

lst = [1,2,3,4,4,5,2,2,1,10,2,2,2,2]
max = 0
second = 0
for i in lst:
    if i > max:
        second = max
        max = i 

print(max, second)


   