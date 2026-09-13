import numpy as np

arr2d=np.array([[1,2,3],[4,5,6]])
print("2D ARRAY:")
print(arr2d)

print("SIZE:")
print(arr2d.shape)  #(row,col)

print("NO OF ELEMENTS:")
print(arr2d.size)

arr3d=np.array([[[1,2,6],[34,5,6]]])
print("NO OF DIMENSIONS:")
print(arr3d.ndim)

print("DATA TYPE OF ELEMENTS:")
print(arr3d.dtype)

arr=np.array([1.1,2.5,6.7])
intarr=arr.astype(int)
print("Type Cast:")
print(intarr)
print(intarr.dtype)
