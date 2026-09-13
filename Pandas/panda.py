import pandas as pd

data = {
    'Name': ['Aisha', 'Bilal', 'Cathy', 'Danish'],
    'Maths': [88, 76, 95, 60],
    'Science': [92, 81, 89, 70]
}

df = pd.DataFrame(data)
print(df)
#task 1
df['Total'] = df['Maths'] + df['Science']
print(df)
#task 2
top_student = df[df['Total'] == df['Total'].max()]
print(top_student)

df.to_csv('results.csv', index=False)
# Task:
# 1. Add a column called 'Total' = Maths + Science
# 2. Find the student with the highest Total
# 3. Save the result as "results.csv"