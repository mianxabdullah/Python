import pandas as pd

data1= {
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Ahmed", "Sara", "Zara"]
}
df1=pd.DataFrame(data1)

data2= {
     "ID": [2, 3, 4, 5],
    "Salary": [30000, 40000, 50000, 60000]
}
df2=pd.DataFrame(data2)

#1. Inner Join (only matching IDs in both)
merged = pd.merge(df1, df2, on="ID", how="inner")
print("Inner Join :")
print(merged)

#2. Left Join (all from df1, add match from df2)
merged1 = pd.merge(df1, df2, on="ID", how="left")
print("Left Join :")
print(merged1)

#3. Right Join (all from df2, add match from df1)
merged2 = pd.merge(df1, df2, on="ID", how="right")
print("Right Join :")
print(merged2)

#4. Outer Join (all from both, fill missing with NaN)
merged3 = pd.merge(df1, df2, on="ID", how="outer")
print("Outer Join :")
print(merged3)