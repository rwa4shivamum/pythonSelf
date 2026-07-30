#List Comprehension (to compression the multiple line of code into single line)
# [value for var in collection]
# [value for var in collection if]

l = [1,2,3,4]
ans = []
for i in l:
    ans.append(i ** 2)
print(ans)

ans2 = [i**2 for i in l]
print(ans2)

ans3 = [i for i in l if i%2==1 ]
print(ans3)