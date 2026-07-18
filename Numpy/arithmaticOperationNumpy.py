import numpy as np;

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# #scalar broadcasting
# a = np.array([1,2,3])

# print(a + 10) #[11,12,13]
# print(a * 2) #[2,4,6]


#matrix Multiplication
a = np.array([
              [1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])
#firstRow:[1,2],*firstColumn:[5,7] = 1*5+2*7 = [19, ]
#firstRow:[1,2],*secndColumn:[6,8] = 1*6+2*8 = [19,22]
#secondRow:[3,4],*firstColumn:[5,7] = 3*5+4*7 = [43, ]
#secondRow:[3,4],*secondColumn:[6,8] = 3*6+4*8 = [[19,22],[43,50]]
print(np.dot(a,b))
print(a @ b)

#power and Square Root
a = np.array([1,4,9])

print(np.sqrt(a)) #[1,2,3]
print(np.power(a,2))

#concatination

a = np.array([1,2])
b = np.array([3,4])

print(np.concatenate((a,b)))

a = np.array([1,2])
b = np.array([3,4])

print(np.vstack((a,b)))#[[1 2]
                       # [3 4]]
print(np.hstack((a,b))) #[1 2 3 4]

arr = np.array([1,2,3,4,5,6])

print(np.split(arr, 3))#[array([1, 2]), array([3, 4]), array([5, 6])]


arr1 = np.array([10,20,30,40,50])

print(np.where(arr1 > 25))#return index postion where (array([2, 3, 4]),)

arr = np.array([50, 20, 40, 10])

print(np.sort(arr))        # ascending [10 20 40 50]
print(np.sort(arr)[::-1])  # descending [50 40 20 10]

arr = np.array([10, 25, 30, 15, 50])

#filtering
print(arr[arr > 20])#[25 30 50]

#aggregation = summarize the data
arr = np.array([10, 20, 30, 40])

print(np.sum(arr))   # 100
print(np.mean(arr))  # 25
print(np.max(arr))   # 40
print(np.min(arr))   # 10

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(matrix, axis=0))  # column-wise [5 7 9]
print(np.sum(matrix, axis=1))  # row-wise [ 6 15]



#statistical Functions Used to analyze data distribution
arr = np.array([10, 20, 30, 40, 50])

print(np.mean(arr))    # average
print(np.median(arr))  # middle value
print(np.std(arr))     # spread
print(np.var(arr))     # variance


print(np.percentile(arr, 50))  # median
print(np.percentile(arr, 25))