from sklearn.preprocessing import LabelEncoder
import pandas as pd
#label encoder is used for columns having binary data (yes/no,acccept/reject) and it converts them into 0 and 1(numerical data) and it is used for columns having more than 2 categories (like fuel type, selling type, transmission) and it converts them into numerical data by assigning a unique integer to each category.
#used for only binary data
df=pd.read_csv("car data.csv")
df_label=df.copy()
le=LabelEncoder()
df_label['fuel_type_encoded']=le.fit_transform(df_label['Fuel_Type'])
df_label['Selling_type_encoded']=le.fit_transform(df_label['Selling_type'])
df_label['Transmission_encoded']=le.fit_transform(df_label['Transmission'])
#print(df_label[['Fuel_Type','Selling_type','Transmission','fuel_type_encoded','Selling_type_encoded','Transmission_encoded']].head())

#one hot encoding is used for columns having more than 2 categories and it creates new binary columns for each category and assigns 1 or 0 to indicate the presence or absence of that category in the original column.
# encode in series of true false or 0 and 1   like  city=[0,0,1,0]
df_encoded=pd.get_dummies(df,columns=['Car_Name','Year','Selling_Price','Present_Price','Driven_kms'])
#get_dummies is used to perform one hot encoding on the specified columns and it creates new binary columns for each category in those columns and assigns 1 or 0 to indicate the presence or absence of that category in the original column.
print(df_encoded.head())
