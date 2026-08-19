import matplotlib.pyplot as plt

ages = [
    18, 19, 20, 20, 21,
    21, 22, 22, 23, 24,
    25, 25, 26, 28, 30
]

plt.hist(ages, bins=5)


plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()