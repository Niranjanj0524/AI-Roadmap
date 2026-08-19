import matplotlib.pyplot as plt

ages = [18, 19, 20, 20, 21, 22, 22, 23, 24, 25]
hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 62, 70, 78, 88]
salaries = [25000, 28000, 30000, 32000, 35000, 36000, 38000, 40000, 90000]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].hist(ages, bins=8, color='skyblue', edgecolor='black', rwidth=0.9)
axes[0].set_title('Histogram of Ages')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')

axes[1].scatter(hours, marks, color='g', marker='o', s=100)
axes[1].set_title('Scatter Plot: Hours vs Marks')
axes[1].set_xlabel('Study Hours')
axes[1].set_ylabel('Marks Obtained')
axes[1].grid(True, linestyle='--', alpha=0.6)

axes[2].boxplot(salaries, patch_artist=True, boxprops=dict(facecolor='lightcoral'))
axes[2].set_title('Box Plot of Salaries')
axes[2].set_ylabel('Salary (in ₹)')
axes[2].set_xticklabels(['Salaries'])

plt.tight_layout()

plt.show()
