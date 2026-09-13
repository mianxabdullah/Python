import pandas as pd

#  df=pd.read_excel("SampleSuperstore.xlsx") #pass name as string
#  df=pd.read_csv("results.csv") #, encoding=utf-8 or encoding=latin1) 
df=pd.read_json("sample_Data.json")

#print(df)  to display whole record/file

print(df.head(2))  #head(n) gives n rows from top 
print("from bottom: ") # if n not specified default =5
print(df.tail(2)) #tail(n) gives n rows from bottom

print(df.info())

