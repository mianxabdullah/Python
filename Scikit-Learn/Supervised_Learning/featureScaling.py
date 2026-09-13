# Feature Scaling is used to scale values of features(columns) b/w 0 and 1 so that model doesnt give more importance to features having higher values and it is used to improve the performance of the model and it is used to make the model converge faster.
from sklearn import StandardScaler, MinMaxScaler
import pandas as pd
df=pd.read_csv("car data.csv")

#In standard scaler mean =0 and standard deviation =1 and it scales the data by removing the mean and scaling to unit variance. It is used when the data is normally distributed(bell curved) and it is sensitive to outliers.
#z=(x-mean)/std
scaler=StandardScaler()
X_scaled=scaler.fit_transform(df[['Present_Price']])

#In min max scaler it scales the data to a fixed range between 0 and 1 and it has no negative values. It is used when the data is not normally distributed and it is not sensitive to outliers.
#x_scaled=(x-x_min)/(x_max-x_min)
minmax_scaler=MinMaxScaler()
X_minmax_scaled=minmax_scaler.fit_transform(df[['Present_Price']])
