age = 21
#ternary Operator
print("isAdult") if age > 18 else print("Not Adult")
#WAP to print 1 to 10 number
i = 1
while(i<10):
    print(i)
    
for i in "Dhruv":
    print(i)
    
#Range Function -> range
"""
range([start], end, [step])
-- start is optional, default is 0
--end is mandatory
--step is optiona, deafult is 1
"""
for i in range(0,9,1):
    print(i)


#control Statement
'''
1.break - To terminate the current block (for,while works both)
2.continue - To skip the current iteration (for only)
3.Pass - It is placeholder used for just syntactical code completion

'''

for i in range(1,11):
    if i==5:
        pass #here Idk what gonna write to complete this syntax we used pass here
    print(i)

"""
here pass only used for syntax completion if we won't use pass then we get error just pass that if condtion we use 'pass' syntax
"""
