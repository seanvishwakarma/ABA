
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("customer_data.csv")

# Descriptive Statistics
print("Mean:")
print(data["PurchaseAmount"].mean())

print("\nMedian:")
print(data["PurchaseAmount"].median())

print("\nMode:")
print(data["PurchaseAmount"].mode())

print("\nVariance:")
print(data["PurchaseAmount"].var())

print("\nStandard Deviation:")
print(data["PurchaseAmount"].std())

# Histogram
plt.hist(data["PurchaseAmount"], bins=5)
plt.title("Histogram of Purchase Amount")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Box Plot
plt.boxplot(data["PurchaseAmount"])
plt.title("Box Plot of Purchase Amount")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.show()
