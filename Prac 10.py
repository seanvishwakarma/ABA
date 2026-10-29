
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 1. Regression Analysis
X = [[10], [20], [30], [40], [50]]
Y = [100, 150, 200, 250, 300]

model = LinearRegression()
model.fit(X, Y)

prediction = model.predict([[60]])

print("Regression Analysis")
print("Predicted Sales =", prediction)

# 2. Time Series Forecasting
sales = [120, 135, 150, 160, 175, 190]

model = ExponentialSmoothing(sales)
fit = model.fit()

forecast = fit.forecast(3)

print("\nTime Series Forecasting")
print("Forecast Values =", forecast)
