# for i in range(3):
#     print(i)
# else:
#     print("done")

# for i in range(3):
#     if i==2:
#         print(i)
#         break
# else:
#     print("Loop finished") why this else won't work

# i = 0
# while i<5:
#     print(i)
#     i+=1

# for i in range(1,11):
#     print(i)
#     i+=2


# for i in range(5,0,-1):
#     print(i)

# i=5
# while(i>0):
#     print(i)
#     i -=1

# for i in range(5,0,-2):
#     print(i)

# for i in "1231bc":
#     print(i)

# i = 1
# while i = 10:
#     i += 2
# for i in range(1):
#     print("Hi")

# print(list(range(10,0,-1))) #prblm 13
# for i in range(1, 10, 2):
#     print(i)

# for i in range(-5): #range(0, -5, 1)
#     print(i)

# for i in range(5, -5, -1):
#     print(i, end=" ")

# for i in range(-3, 3, 1):
#     print(i, end=" ")

# for i in range(0):
#     print("Hello")
# else:
#     print("Done")
# for i in range(3):
#     for j in range(i):
#         print(i, j)

# for i in range(1, 11, 3):
#     print(i, end=" ")

# print(list(range(10, 10)))


lst = []

# for i in range(1,4):
#     lst.append(i)

# print(lst)
# lst = []
# lst5 = []
# for i in range(0,100):
#     if i%3==0:
#         lst.append(i)
#     elif i%5==0:
#         lst5.append(i)

# print(lst)
# print(lst5)

# print([x if x%2==0 else -x for x in range(5)])

# print([(i,j) for i in range(2) for j in range(3)])

# for i in range(3):
#     print(i)
#     i = 5

# lst = [1,2,5,3]
# for i in lst:
#     print(i)

# for i in range(5):
#     if i == 2:
#        continue
#     print(i)
# else:
#     print("Done")

# lst = [1,2,3,4,5]
# sum = 0
# for i in lst:
#     sum += i

# print(sum)
# n = 121
# num = n
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse == n)


# str = "jahdjkhsbfdoqiuwey"
# count = 0
# for i in str:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         count += 1
    
# print(count)

# lst = []

# def isPrime(n):
#     count = 0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count += 1

#     if(count == 2):
#         return True
#     else:
#         return False

# print(isPrime(2))
# # for i in range(1,101):
# #     if(isPrime(i)):
# #         lst.append(i)

# print(lst)

#list comprehension
# [expression for item in iterable]

# print([i for i in range(5)])

# print([i for i in range(10) if i%2==0])

print([i if i%2==0 else 2 for i in range(20)])
print([i for i in range(10) if i > 5 ])
print([i if i>0  else 0 for i in range(10,-10,-1)])
lst = ["shit", "sjs", "sj", "jhdsfh", "uih"]
print([i for i in lst if len(i)>3])
# print(("E" if i%2==0 else "O" for i in range(1,10)))
print([i for i in range(20) if i % 2 == 0 and i % 3 == 0])