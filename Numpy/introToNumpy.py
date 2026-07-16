#intro to Numpy
#what is numpy(Numerical Python) is Library used for:
#fast Calculation
#Working with arrays(like advanced List)
#Data science & Machine Learning

# | Feature    | List        | NumPy      |
# | ---------- | ----------- | ---------- |
# | Speed      | Slow        |⚡ Fast    |
# | Memory     | High        | Efficient  |
# | Operations | Manual loop | Vectorized |

import numpy as np

arr = np.array([1,2,3,4])
print(arr)

#pip install numpy to install the packages
# to check weather which version and which packages install
# python -c "import numpy; print(numpy.__version__)"
weights = np.array([0.2, 0.5, 0.1])
inputs = np.array([10, 20, 30])

output = np.dot(weights, inputs)
print(output)

arr1 = np.array([1,2,3,4])
arr2 = np.array([2,3,4,5])

print(arr1 + arr2)
#creatino of numpy array
arryb = np.array([[1, 2], [3, 4]])
print(arryb)
print(arryb[0])
print(arryb[1])
print(arryb[-1][0])
#special Arrays
print(np.zeros((2,3)))
print(np.ones((2,2)))
print(np.arange(0,10,2))
print(np.linspace(0,2,10))

#2D indexing

arr3 = np.array([[10,20,30,40,50],[10,20,30,40,50]])

print(arr3[0],[1])#same below
print(arr3[0,1])#same above

#6.slicing in numpy
#[start: end : step]

#1D slicing
arr = np.array([10,20,30,40,50])
print(arr[0:4:3])
print(arr[::3])
print(arr[:2:1])

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[0:2, 1:3])