
from scipy.optimize import linprog
import random

# 1. Optimization using Linear Programming
c = [-40, -30]

A = [
    [1, 0],
    [0, 1]
]

b = [40, 50]

result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

print("Optimal Solution")
print(result.x)

print("Maximum Profit")
print(-result.fun)


# 2. Simulation
profits = []

for i in range(1000):
    demand = random.randint(50, 150)
    profit = demand * 20
    profits.append(profit)

print("Average Profit =", sum(profits) / len(profits))
