import numpy as np 
arr=np.array([10,20,40,50,60,70,80])
print("original array : \n",arr)
# INSERT Syntax: np.insert(array,index,value)
new_arr=np.insert(arr,2,30)
print("added value :\n",new_arr)

ar=np.array([[1,2],[3,4]])
print("original 2D array : \n",ar)
new_ar=np.insert(ar,1,[5,6],axis=1)
print("added value in 2D :\n",new_ar)

# APPEND Syntax: np.append(array,value)
print("before append: \n",arr)
newArr=np.insert(arr,2,30)
newArr=np.append(arr,[90,100])
print("appended array: \n",newArr)

#Concatenation:
one=np.array([1,2,3,4,5])
two=np.array([6,7,8,9,10])
new=np.concatenate((one,two))
print("Concatenated :\n",new)

#Remove\Delete:
newNEW=np.delete(new,1)
print("Deleted :\n",newNEW)

array=np.array([[1,2],[3,4],[5,6]])
newArray=np.delete(array,0,axis=0)
print("Deleted 2D :\n",newArray)
# Stacking :
"""
vstack->row wise
hstack->col wise
"""
print("vstack :\n",np.vstack((one,two)))
print("hstack :\n",np.hstack((one,two)))

# SPLITTING:
"""
np.split() equal splitting
np.hsplit() horizontal
np.vsplit() vertical
"""
sp=np.array([1,2,3,4,5,6,7,8,9,10])
print("Splitted Arrays :\n",np.split(sp,5))
#print("Splitted Arrays :\n",np.vsplit(sp,5)) works on 2D arrays
print("Splitted Arrays :\n",np.hsplit(sp,5))
