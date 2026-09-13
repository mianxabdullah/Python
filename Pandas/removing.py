import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","roman","sarim","hooria","dawood"],
    "ID":[10,20,55,46,18,56,39,16]
    ,"age":[19,32,45,23,28,37,12,23],
    "salary":[15000,45000,23000,58000,63000,33000,25000,60000],
    "performance-score":[88,89,78,96,92,81,86,98],
    "rank":["gold","silver","bronze","platinium","gold","silver","bronze","platinium"]
}

df=pd.DataFrame(data)
print(df)

# Removing Single Column
# SYNTAX : df.drop(columns=["col_name"],inplace=true) 
#inplace=true make change in the original data set otherwise a copy is returned
df.drop(columns=["performance-score"],inplace=True)
print("Column Removed :")
print(df)

# Removing Multiple Column
# SYNTAX : df.drop(columns=["col1_name","col2_name"],inplace=true)
df.drop(columns=["age","ID"],inplace=True)
print("Multiple Column Removed :")
print(df)