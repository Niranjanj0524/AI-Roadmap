import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Rohan"],
    "Age": [20, 21, 20, 22, 21],
    "Gender": ["M", "M", "F", "F", "M"],
    "Math": [85, 78, 92, 88, 75],
    "Science": [80, 82, 95, 85, 79],
    "English": [88, 76, 90, 91, 72]
}

df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())