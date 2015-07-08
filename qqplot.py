from __future__ import division
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

n = 100

measurements = [stats.norm.ppf(x/(n+1)) for x in range(1, n+1)]

sample = [np.random.normal() for _ in range(n)]
sample.sort()

plt.scatter(measurements, sample)
plt.title("QQ Plot of random.random data")
plt.axis(xmin = min(measurements) - (.1 * abs(min(measurements))), xmax = max(measurements) + (.1 * abs(max(measurements))), ymin = min(sample) - (.1 * abs(min(sample))), ymax = max(sample) + (.1 * abs(max(sample))))

plt.xlabel("std normal quantiles")
plt.ylabel("sorted sample values")
plt.show()