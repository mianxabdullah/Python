import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","roman","sarim"]
    ,"age":[19,32,45,23,28,37],
    "salary":[15000,45000,23000,60000,63000,33000],
    "performance-score":[88,89,78,96,92,81]
}

df=pd.DataFrame(data)

names=df['name']  #way to access SINGLE column from data 
print(names)      # OR print(df['Col name'])

subset=df["name","age"]  #way to access MULTIPLE column from data
print(subset)           # OR print(df['Col1 name','col2 name'])