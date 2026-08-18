import pandas as pd

df = pd.read_csv("student.csv")
print("\n Complete dataset: ")
print(df)

print("\n First 3 student: ")
print(df.head(3))
print("\n Last 2 student: ")
print(df.tail(2))

print("\n Name & Maths: ")
print(df[["Name", "Math"]])

print("\n maths marks greater than 80: ")
print(df[df["Math"] > 80])

print("\n Females: ")
print(df[df["Gender"] == "F"])

print("\n Maths and Science greater than 80: ")
print(df[(df["Math"] > 80) & (df["Science"] > 80)])

print("\n MAths or Science is greater than 90: ")
print(df[(df["Math"] > 90) | (df["Science"] > 90)])

print("\n Sort by maths marks: ")
print(df.sort_values("Math"))

print("\n sort ascending by maths marks: ")
print(df.sort_values("Math",ascending=False))

print("\n Highest Maths Marks: ", df["Math"].max())

print("\n Avg maths marks: ", df["Math"].mean())

high_math = df[df["Math"] > 80]
high_math.to_csv("high_math_students.csv", index=False)
