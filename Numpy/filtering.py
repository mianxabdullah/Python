import numpy as np
"""Filtering based on conditions"""
arr=np.array([10,20,30,40,50,60,70])
print(arr[arr>20])

print(arr[arr<50])

print(arr[(arr>20)&(arr<50)])