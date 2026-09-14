import pandas as pd
df=pd.read_csv("car data.csv")
print(df.isnull().sum())
# theres no missing value in this dataset but we handle them by dropna or fillna method if there were any missing values.