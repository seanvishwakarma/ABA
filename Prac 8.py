
import numpy as np
from scipy import stats

# Sample data
data = [45, 50, 55, 60, 65, 70, 75]

# Calculate mean
mean = np.mean(data)

# Calculate 95% Confidence Interval
ci = stats.t.interval(
    confidence=0.95,
    df=len(data) - 1,
    loc=mean,
    scale=stats.sem(data)
)

# Display result
print("95% Confidence Interval:", ci)
