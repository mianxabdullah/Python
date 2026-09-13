import pandas as pd

import numpy as np

df = pd.read_csv("employees_with_errors.csv")
print(df.head())
print("Count of missing values:\n", df.isnull().sum())

# Fill missing Salary values with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill numeric missing values with their mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing text values with 'Unknown'
df.fillna('Unknown', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Replace negative Salary values with column mean
df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(), df['Salary'])

# Remove outliers beyond 3 standard deviations
salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (salary_std * 3)
upper_bound = salary_mean + (salary_std * 3)
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("Data cleaning complete. Saved as 'cleaned_data.csv'")