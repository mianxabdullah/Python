import numpy as np

arr=np.array([10,20,30,40,50,60])
reshape_arr=arr.reshape(2,3) #it effects the original data
print(reshape_arr)

"""
.ravel()->view
.flatten()->copy
"""
a=np.array([[10,20,30],[40,50,60]])
print("original: \n",a)
print(".ravel():",a.ravel())
print(".flatten():",a.flatten())