import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","roman","sarim"]
    ,"age":[19,32,45,23,28,37],
    "salary":[15000,45000,23000,60000,63000,33000],
    "performance-score":[88,89,78,96,92,81]
}

df=pd.DataFrame(data)

#Methods:

print("Description of data :")
print(df.describe())

print("Size of data :")
print(df.shape) #.shape return size of data as tuple (rows,cols)

print("Column names : ")
print(df.columns) #.columns returns all column names

print("from top :")
print(df.head(2))  #head(n) gives n rows from top 

print("from bottom : ") # if n not specified default =5
print(df.tail(2)) #tail(n) gives n rows from bottom

print("Information :")
print(df.info())

# summary of column
mean=df["age"].mean()
min=df["age"].min()
max=df["age"].max()
sum=df["age"].sum()
print(f"Mean of AGE column is :{mean}")
print(f"Minimum of AGE column is :{min}")
print(f"Maximum of AGE column is :{max}")
print(f"Sum of AGE column is :{sum}")