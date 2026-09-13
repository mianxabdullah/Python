import pandas as pd

data={
    "name":["ali","abd","ahmad","akmal","roman","sarim","hooria","dawood"]
    ,"age":[19,32,45,23,28,37,12,23],
    "salary":[15000,45000,23000,58000,63000,33000,25000,60000],
    "performance-score":[88,89,78,96,92,81,86,98]
}
df=pd.DataFrame(data)

highSalary=df[df["salary"]>50000]  # Single condition
print("emplyees with salaries>50000 are :")
print(highSalary)

abc=df[(df["salary"]>30000) & (df["age"]>25) ]  # MULTIPLE condition
print("emplyees with salaries>30000 & age>25 :")
print(abc)

xyz=df[(df["salary"]>50000) | (df["performance-score"]>90) ]  # MULTIPLE condition
print("emplyees with salaries>50000 & performance-score>90 :")
print(xyz)





