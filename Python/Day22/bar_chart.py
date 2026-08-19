import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
sales = [50, 120, 80, 60]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")

plt.savefig("sales_chart.png")

plt.show()