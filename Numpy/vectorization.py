import numpy as np 
"""
Vectorization = Perform array operations without loops.

Broadcasting = Make shapes compatible so vectorized operations can still run.

"""
arr=np.array([1,2,3])
arr2=np.array([4,5,6])
res = arr + arr2
res2 = arr * 100 
print(res)
print(res2)