from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = [
    [500],
    [1000],
    [1500],
    [2000],
    [2500],
    [3000]
]

y = [25, 50, 75, 100, 125, 150]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Training Features:", X_train)
print("Testing Features:", X_test)
print("Actual Prices:", y_test)
print("Predicted Prices:", prediction)