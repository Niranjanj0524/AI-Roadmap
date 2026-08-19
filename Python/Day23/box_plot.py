import matplotlib.pyplot as plt

salaries = [
    25000, 28000, 30000,
    32000, 35000, 36000,
    38000, 40000, 42000,
    90000
]

plt.boxplot(salaries)

plt.title("Salary Distribution")
plt.ylabel("Salary")

plt.show()