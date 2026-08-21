from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

X = [
    [500],
    [1000],
    [1500],
    [2000],
    [2500],
    [3000],
    [3500],
    [4000],
    [4500],
    [5000]
]

y = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

prediction = model.predict(X_test)

mae = mean_absolute_error(y_test, prediction)

mse = mean_squared_error(y_test, prediction)

print("Actual Prices:", y_test)
print("Predicted Prices:", prediction)

print("MAE:", mae)
print("MSE:", mse)