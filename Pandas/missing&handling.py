import pandas as pd

data={
    "name":["ali","abd",None,"akmal","roman","sarim","hooria","dawood"],
    "ID":[10,20,None,46,18,56,39,16]
    ,"age":[19,32,None,23,28,37,12,23],
    "salary":[15000,None,23000,58000,63000,33000,25000,60000],
    "performance-score":[88,89,None,96,92,81,86,98],
    "rank":["gold","silver",None,"platinium","gold","silver","bronze","platinium"]
}

df=pd.DataFrame(data)
print("DATA FRAME :")
print(df)

print("isNULL() :")
print(df.isnull()) #true = data missing or null
print("isNULL().sum() :")
print(df.isnull().sum()) # gives the count of missing values in a column

#After detecting missing values NOW, we can handle them in following ways:
# 1. removing data with missing values
# SYNTAX: df.dropna(axis=0,inplace=True) axis 0 for removing from rows and 1 for cols
print("dropna() :")
df.dropna(inplace=True) #removes rows with missing data  
print(df)

# 2. filling data with missing values
# SYNTAX: df.fillna(value,inplace=True) 
print("fillna() :")
df.fillna(0,inplace=True) #removes rows with missing data  
print(df)

df["age"].fillna(df["age"].mean(),inplace=True) #filling missing values in age col with mean of it
print(df)


data1={
    "time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}

d=pd.DataFrame(data1)
print("DATA FRAME before interpolate:")
print(d)

#3. filling data with an estimation assessing the pattern
d.interpolate(method='linear',axis=0,inplace=True)
print("DATA FRAME after interpolate:")
print(d)

