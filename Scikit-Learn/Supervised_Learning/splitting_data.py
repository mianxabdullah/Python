import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

df=pd.read_csv("car data.csv")
print("Standard Scaler :")
df_numeric = df.select_dtypes(include=['number'])
scaler=StandardScaler()
df_scaled=scaler.fit_transform(df_numeric)
df_scaled = pd.DataFrame(df_scaled, columns=df_numeric.columns, index=df_numeric.index)
print(df_scaled.head())   

print("Min Max Scaler :")
minmax_scaler=MinMaxScaler()
df_minmax_scaled=minmax_scaler.fit_transform(df_numeric)    
df_minmax_scaled = pd.DataFrame(df_minmax_scaled, columns=df_numeric.columns, index=df_numeric.index)
print(df_minmax_scaled.head())



X=df_scaled[['Present_Price']]
y=df[['Selling_Price']]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print("X_train :\n",X_train)
print("X_test :\n",X_test)
print("y_train :\n",y_train)
print("y_test :\n",y_test)

