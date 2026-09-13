import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","roman","sarim","hooria","dawood"]
    ,"age":[19,32,45,23,28,37,12,23],
    "salary":[15000,45000,23000,58000,63000,33000,25000,60000],
    "performance-score":[88,89,78,96,92,81,86,98]
}
df=pd.DataFrame(data)
print(df)

# 1 way to add new column
df["bonus"]=df["salary"] * 0.1  # 10% of salary  
print("Data with Added column :")
print(df)

# 2 insert method  df.insert(location,"name",data)
df.insert(0,"ID",[12,30,44,22,45,56,18,29])
print("Data with Insert column :")
print(df)