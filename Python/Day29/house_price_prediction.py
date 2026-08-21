from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error



X = [
    [500, 1, 1],
    [800, 2, 1],
    [1000, 2, 1],
    [1200, 2, 2],
    [1500, 3, 2],
    [1800, 3, 2],
    [2000, 3, 2],
    [2200, 4, 3],
    [2500, 4, 3],
    [3000, 4, 3]
]



y = [25, 40, 50, 60, 75, 90, 100, 115, 130, 150]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



model = LinearRegression()



model.fit(X_train, y_train)



predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)



print("===== HOUSE PRICE PREDICTION =====")

print("\nActual Prices:")
print(y_test)

print("\nPredicted Prices:")
print(predictions)

print("\nMean Absolute Error (MAE):")
print(mae)

print("\nMean Squared Error (MSE):")
print(mse)


new_house = [[1700, 3, 2]]

predicted_price = model.predict(new_house)

print("\nNew House Details:")
print("Area: 1700 sq.ft")
print("Bedrooms: 3")
print("Bathrooms: 2")

print("\nPredicted House Price:")
print(predicted_price[0], "Lakhs")