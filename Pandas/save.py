import pandas as pd
data={
    "nam":["abd","talha","musify","sheraz"],
    "unis":["pucit","fast","superior","none"],
    "ages":[17,19,20,18]
}
df=pd.DataFrame(data)
print(df)

#df.to_csv("out.csv",index=False) #normally it shows numbering of rows if you dont want the use index=false
df.to_excel("out.xlsx",index=False)
#df.to_json("out.jsom",index=False)