import numpy as np
# 1D array :
arr=np.array([1,2,3,4,5]) 
print("1D ARRAY:")
print(arr)
# 2D array :
arr2d=np.array([[1,2,3],[4,5,6]])
print("2D ARRAY:")
print(arr2d)

zerosArr=np.zeros(3) #3=size
print("ZEROS ARRAY:")
print(zerosArr)

onesArr=np.ones((2,3)) #size=2x3
print("ONES ARRAY:")
print(onesArr)

filledArr=np.full((2,2),5)  #(size,value)
print("FILLED ARRAY:")
print(filledArr)

sequence=np.arange(1,10,3) #(start,stop,step)
print("SEQUENCE ARRAY:")
print(sequence)

identityMATRIX=np.eye(3) 
print("IDENTITY MATRIX ARRAY:")
print(identityMATRIX)


