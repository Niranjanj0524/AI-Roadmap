import pandas as pd

df = pd.read_csv("employees.csv")

print(df.head(1))
print(df.info())

print("\nNumber of mising values: ", df.isna().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
print("after filled missing age:\n", df['Age'])

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("after filled missing Salary:\n", df['Salary'])

duplicate_rows = df.duplicated().sum()
print("Duplicate rows: ",duplicate_rows)

df = df.drop_duplicates()
print(len(df))

df['Gender'] = df['Gender'].replace({
    'Male' : 'male',
    'M' : 'male',
    'Female' : 'female',
    'F' : 'female'
})
print(df['Gender'].unique())

df['Name'] = df['Name'].str.strip()
df['Name'] = df['Name'].str.replace(r'\s+', ' ', regex=True)
print(df['Name'].head())
print(df.dtypes)

df['Salary_Per_Year'] = (df['Salary']/df['Experience'])

df['Age_Category'] = df['Age'].apply(
    lambda x: "Young" if x < 25 else "Experienced"
)

columns_to_drop = ['Unnecessary_Col1', 'Unnecessary_Col2']
df = df.drop(columns=columns_to_drop, errors='ignore')

df = df.rename(columns={'Age_Category': 'age_cate'})

print(df.shape)
print(df.isnull().sum())

df.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned dataset successfully saved as 'cleaned_dataset.csv'!")


final_ml_df = pd.get_dummies(df, drop_first=True)

print("--- Final Dataset Preview for ML ---")
print(final_ml_df)
