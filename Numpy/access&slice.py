import numpy as np
"""
arr[index] for 1D
arr[row,col] for 2D
"""
arr=np.array([10,20,30,40,50,60,70])
print(arr[0])
print(arr[-1])

ar=np.array([[1,2,3],[4,5,6]])
print(ar)
print(ar[0,2])
print(ar[1,1])

# SLICING :
"""
SYNTAX: arr[start:stop:step]
"""
print(arr[:6]) # 0 to 5
print(arr[2:]) # 2 to n-1 
print(arr[::2]) # 0 to n-1 with a step(increment) of 2
print(arr[0:7:1]) 
print(arr[::-1]) # negative indexing (reverses the array)

#FANCY INDEXING selecting multiple indexes at once.
print("aa",arr[[1,4,5]])