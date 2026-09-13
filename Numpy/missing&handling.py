import numpy as np

#finding missing value 
arr=np.array([1,2,np.nan,3,np.nan,5])
print("finding missing value",np.isnan(arr)) # true = missing

# replacing missing value with some value or default 0
arr2=np.nan_to_num(arr,nan=5)
print("replacing missing value",arr2)

#finding infinite value 
arr3=np.array([1,2,np.inf,3,-np.inf,5])
print("finding infinite value ",np.isinf(arr3)) # true = missing

# replacing infinite value with some value 
arr4=np.nan_to_num(arr3,posinf=100 ,neginf=-100)
print("replacing infinite values",arr4)

