
import random
import numpy as np
import matplotlib.pyplot as plt

# 1. Probability Simulation using Dice
rolls = 1000
results = []

for i in range(rolls):
    results.append(random.randint(1, 6))

print("Dice Roll Probabilities")

for num in range(1, 7):
    probability = results.count(num) / rolls
    print("Probability of", num, "=", probability)

# 2. Generate Probability Distributions
normal_data = np.random.normal(50, 10, 1000)
uniform_data = np.random.uniform(0, 100, 1000)
exponential_data = np.random.exponential(5, 1000)

print("\nNormal Distribution Sample")
print(normal_data[:10])

print("\nUniform Distribution Sample")
print(uniform_data[:10])

print("\nExponential Distribution Sample")
print(exponential_data[:10])

# 3. Plot Normal Distribution
plt.hist(normal_data, bins=20)
plt.title("Normal Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
