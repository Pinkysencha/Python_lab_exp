import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', np.nan],
    'Age': [25, 30, np.nan, 45, 25, 35],
    'Salary': [50000, 60000, 70000, 80000, 50000, 1200000],
    'Joined_Date': ['2020-01-01', '2021-06-15', '2019-11-20', '2022-03-05', '2020-01-01', '2023-01-10']
}
df = pd.DataFrame(data)

df = df.drop_duplicates()

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Name'] = df['Name'].fillna('Unknown')

df['Joined_Date'] = pd.to_datetime(df['Joined_Date'])

df['Salary'] = df['Salary'].clip(upper=150000)

print("Data Overview ")
print(df.info())

print("\n Summary Statistics")
print(df.describe())

print("\n Missing Values Count ")
print(df.isnull().sum())

print("\n Grouped Analysis")
print(df.groupby('Name')['Salary'].mean())
