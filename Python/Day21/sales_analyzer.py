import pandas as pd

df = pd.read_csv("sales.csv")
print(df)

df['Total_Sales'] = (df['Quantity'] * df['Price'])
print("\nTotal Sales:\n", df['Total_Sales'])

print(df.head())
print(df.info())
print(df.describe())

print("\nCheck Missing Values: \n",df.isnull().sum())

print("\nCheck Duplicate Values: \n",df.duplicated().sum())

total_sales = df["Total_Sales"].sum()

print("\nTotal Sales:", total_sales)

average_sales = df["Total_Sales"].mean()

print("\nAverage Sales:", average_sales)

highest_sale = df['Total_Sales'].max()
print("\nHighest Sales: ", highest_sale)

employee_sales = df.groupby("Employee")["Total_Sales"].sum()
print("\nEmployee sales: \n",employee_sales)

product_sales = df.groupby("Product")["Total_Sales"].sum()
print("\nProduct Sales: \n",product_sales)

category_sales = df.groupby(
    "Category"
)["Total_Sales"].sum()
print("\nSales by Category : \n",category_sales)

print(df.sort_values("Total_Sales",ascending=False))

best_employee = (
    df.groupby("Employee")["Total_Sales"]
    .sum()
    .idxmax()
)
print("\nBest Employee:", best_employee)

best_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)
print("\nBest Product:", best_product)

df.to_csv("analyzed_sales.csv",index=False)