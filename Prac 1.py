
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Display first records
print("First Five Records")
print(data.head())

# Dataset information
print("\nDataset Information")
data.info()

# Missing values
print("\nMissing Values")
print(data.isnull().sum())

# Summary statistics
print("\nSummary Statistics")
print(data.describe())

# Average Purchase Amount
avg_purchase = data["PurchaseAmount"].mean()
print("\nAverage Purchase:", avg_purchase)

# Sales by City
city_sales = data.groupby("City")["PurchaseAmount"].sum()

print("\nSales by City")
print(city_sales)

# Visualization
city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
