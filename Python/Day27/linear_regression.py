from sklearn.linear_model import LinearRegression

X = [[500], [1000], [1500], [2000], [2500]]
y = [25, 50, 75, 100, 125]

model = LinearRegression()

model.fit(X,y)

prediction = model.predict([[1800]])

print("Predicted Price:", prediction)