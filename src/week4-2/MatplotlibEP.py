# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

# listKO = []
# closeMeansKO = tempkodf.groupby('month').mean().close
# for i in range(1, 13):
#     listKO.append(closeMeansKO[i])
# listKOIndex = closeMeansKO.index
# 折线图
# plt.plot(listKOIndex, listKO)
# 散点图
# plt.plot(listKOIndex,listKO, 'o')
# plt.plot(listKOIndex,listKO, 'rD')
# plt.plot(listKOIndex,listKO, 'g--')
# 柱状图
# plt.bar(listKOIndex,listKO)
# plt.show()

t = np.arange(0., 4., 0.1)
plt.plot(t, t, t, t + 2, t, t ** 2)
pl.plot(t, t, t, t + 2, t, t ** 2)
plt.show()
pl.show()
