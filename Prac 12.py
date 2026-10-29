
from scipy.stats import f_oneway

# Define three groups
group1 = [45, 50, 55, 60]
group2 = [60, 65, 70, 75]
group3 = [80, 85, 90, 95]

# Perform one-way ANOVA test
f_stat, p_value = f_oneway(group1, group2, group3)

# Display results
print("F Statistic =", f_stat)
print("P Value =", p_value)
