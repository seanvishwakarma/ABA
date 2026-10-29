
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("advertising_data.csv")

# Correlation Analysis
correlation = data["Advertising_Expense"].corr(data["Sales_Revenue"])
print("Correlation Coefficient =", correlation)

# Regression Analysis
X = data[["Advertising_Expense"]]
Y = data["Sales_Revenue"]

model = LinearRegression()
model.fit(X, Y)

# Predict sales revenue
predictions = model.predict(X)

# Display graph
plt.scatter(X, Y)
plt.plot(X, predictions)
plt.xlabel("Advertising Expense")
plt.ylabel("Sales Revenue")
plt.title("Regression Analysis")
plt.tight_layout()
plt.show()

# Display intercept and slope
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
