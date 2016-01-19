import numpy as np
from matplotlib.finance import _quotes_historical_yahoo


x = ([(1, 3, 6, 100), (0, 5, 6, 8), (3, 2, 2, 8)])
# x = np.array([(1, 3, 6, 100), (0, 5, 6, 8)])
y = [99, 99]

print len(np.diff(x, axis=0))
print np.diff(x, axis=0)[0][2]
for j in range(2):
    y[j] = np.diff(x, axis=0)[j][2]

print y
