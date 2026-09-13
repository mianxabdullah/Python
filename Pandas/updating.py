import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","roman","sarim","hooria","dawood"]
    ,"age":[19,32,45,23,28,37,12,23],
    "salary":[15000,45000,23000,58000,63000,33000,25000,60000],
    "performance-score":[88,89,78,96,92,81,86,98]
}

df=pd.DataFrame(data)
print(df)

#updating perticular cell
# SYNTAX : df.loc[row_index,"col_name"]=new_value
df.loc[0,"salary"]=25000
print("Updated Cell :")
print(df)

#updating whole column
#increasing salary by 10%
df["salary"]=df["salary"]*1.1
print("Updated Column :")
print(df)



