
import numpy as np

# Generate population of 1000 random numbers
population = np.random.randint(1, 100, 1000)

# Select a random sample of 50 numbers
sample = np.random.choice(population, 50)

# Calculate and display means
print("Sample Mean =", np.mean(sample))
print("Population Mean =", np.mean(population))
