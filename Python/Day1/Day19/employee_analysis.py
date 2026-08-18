import pandas as pd
import numpy as np

df_emp = pd.read_csv("employees.csv")
df_dept = pd.read_csv("departments.csv")

print("Employees DataFrame:\n", df_emp)
print("\nDepartments DataFrame:\n", df_dept)

print("\n" + "="*50 + "\n")

print("Average Salary by DepartmentID:\n", df_emp.groupby('DepartmentID')['Salary'].mean())

print("\nTotal Salary by DepartmentID:\n", df_emp.groupby('DepartmentID')['Salary'].sum())

print("\nCount Employee In each DepartmentID:\n", df_emp.groupby('DepartmentID')['EmployeeID'].count())

print("\n Average Experiance by DepartmentID:\n", df_emp.groupby('DepartmentID')['Experience'].mean())

print("\nSalary aggregated (mean, sum, count) by DepartmentID:\n", df_emp.groupby('DepartmentID')['Salary'].agg(['mean', 'sum', 'count']))

print("\n" + "="*50 + "\n")

df_merged = pd.merge(df_emp, df_dept, on='DepartmentID', how='left')
print("\nComplete merged dataset: ", df_merged)

print("\nEmployee Names with their Departments:\n", df_merged[['Name','Department']])

print("\nAverage Salary by Department Name:\n", df_merged.groupby('Department')['Salary'].mean())

print("\n" + "="*50 + "\n")

print("Missing values count per column:\n", df_emp.isnull().sum())

missing_cols = df_emp.columns[df_emp.isnull().any()].tolist()
print("\nColumns containing missing values:", missing_cols)

df_drop = df_emp.dropna()
print("\nDataset after removing rows with missing values:\n", df_drop)

df_fill_zero = df_emp.copy()
df_fill_zero['Salary'] = df_fill_zero['Salary'].fillna(0)
print("\nDataset after filling missing Salary with 0:\n", df_fill_zero)

df_fill_mean = df_emp.copy()
mean_salary = df_emp['Salary'].mean()
df_fill_mean['Salary'] = df_fill_mean['Salary'].fillna(mean_salary)
print(f"\nDataset after filling missing Salary with average ({mean_salary}):\n", df_fill_mean)
print("\n" + "="*50 + "\n")

df_combined = pd.merge(df_fill_mean, df_dept, on='DepartmentID', how='left')
print("Highest Salary by Department:\n", df_combined.groupby('Department')['Salary'].max())

print("Lowest Salary by Department:\n", df_combined.groupby('Department')['Salary'].min())

print("\nAverage Experience by Department:\n", df_combined.groupby('Department')['Experience'].mean())

df_combined.to_csv('cleaned_employees.csv', index=False)
print("\nFinal Cleaned Employee Dataset saved as 'cleaned_employees.csv':\n", df_combined)
