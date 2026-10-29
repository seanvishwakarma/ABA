
from scipy.stats import ttest_1samp

# Sample sales data
sales = [5100, 4950, 5050, 5200, 5000]

# Perform one-sample t-test
t_stat, p_value = ttest_1samp(sales, 5000)

# Display results
print("T Statistic =", t_stat)
print("P Value =", p_value)
