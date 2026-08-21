from sklearn.linear_model import LinearRegression

X = [
    [1000, 2, 1],
    [1500, 3, 2],
    [2000, 3, 2],
    [2500, 4, 3],
    [3000, 4, 3]
]

y = [50, 75, 100, 125, 150]

model = LinearRegression()

model.fit(X,y)

prediction = model.predict([[2200,3,2]])

print("Price: ", prediction)