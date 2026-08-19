import matplotlib.pyplot as plt

categories = ["IT", "HR", "Finance", "Sales"]
employees = [40, 20, 15, 25]

plt.pie(
    employees,
    labels=categories,
    autopct="%1.1f%%"
)

plt.title("Employee Distribution")

plt.show()