import numpy as np

a=np.array([10,20,30,40,50])

#single broadcasting:
result=a*3  #does not require loops as traditional arrays does
print(result)

# 1D to 2D:
b=np.array([[1,2,3],[4,5,6]])
c=np.array([10,20,30])
d=b+c
print(d)

# incompatible (error)
"""
arr=np.array([[1,2,3],[4,5,6]]) shape(2,3)
arr2=np.array([10,20]) shape(2)
res=arr+arr2 raises error
print(res )

"""