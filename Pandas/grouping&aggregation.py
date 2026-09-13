import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","abd","sarim","hooria","dawood"],
    "ID":[10,20,55,46,18,56,39,16]
    ,"age":[19,32,45,32,32,37,45,23],
    "salary":[15000,45000,23000,58000,63000,33000,25000,60000],
    "performance-score":[88,89,78,96,92,81,86,98],
    "rank":["gold","silver","bronze","platinium","gold","silver","bronze","platinium"]
}

df=pd.DataFrame(data)
print("DATA FRAME :")
print(df)

#grouping of single column means inside a column similar entries are grouped
grp = df.groupby("rank")
print(grp.groups)
print(grp.get_group('gold'))

#grouping of multiple columns
grup = df.groupby(["name","age"])
print(grup.groups)
print(grup.get_group(("abd",32)))

#single column grouping and AGGREGATION i.e., (  [""].func()  )
grouped = df.groupby("age")["salary"].sum()
print("age and salary are grouped")
print(grouped)

#multi columns grouping and aggregation
group = df.groupby(["age","name"])["salary"].sum()
print("age,name and salary are grouped")
print(group)