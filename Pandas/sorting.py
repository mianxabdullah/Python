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
print("DATA FRAME :")
print(df)
#Sorting  single column
#SYNTAX : df.sort_values(by="column-name",ascending=true/false,inplace=True) true=ascending ,false=descending
df.sort_values(by="age",ascending=True,inplace=True)
print("After Sorting Age :")
print(df)

#sorting multiple column
df.sort_values(by=["age","salary"],ascending=[True,True],inplace=True)
print("After Sorting Age , Salary:")
print(df)