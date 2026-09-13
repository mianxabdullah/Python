import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Ali', 'Ahmed'],
    'Age': [22, 23]
})

df2 = pd.DataFrame({
    'Name': ['Sara', 'Zara'],
    'Age': [21, 24]
})

# Concatenate vertically (axis=0)
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)

# Concatenate vertically (axis=1)
result1 = pd.concat([df1, df2], axis=1, ignore_index=True)
print(result1)