import pandas as pd


mark = pd.Series([80, 75, 90, 85])
print(mark)
print("0th element", mark[0])

marks = pd.Series(
    [80, 75, 90],
    index=["Math", "Science", "English"]
)
print("\n", marks)
print(marks.iloc[1])


marks1 = {
    "Math": 80,
    "Science": 75,
    "English": 90
}
series = pd.Series(marks1)
print("\n", series)


data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [20, 21, 20],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print("\n", df)
print(df["Name"])
print(df["Name"],["Marks"])

print(df.iloc[0, 2])
print(df.shape)
print(df.columns)
print(df.index)
print(df.head(2))
print(df.tail(1))
df.info()
print(df.describe())