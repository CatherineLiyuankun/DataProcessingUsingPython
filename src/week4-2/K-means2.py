# -*- coding: utf-8 -*-
# 按相邻两天的收盘价涨跌规律对2014年第3季度(7月-9月)构成道 琼斯工业指数的30只股票聚类
# Filename: kmeansDJI.py
from matplotlib.finance import _quotes_historical_yahoo
from pylab import *
from scipy.cluster.vq import *
import numpy as np
from datetime import date

today = date.today()
start = (today.year - 2, today.month + 6, today.day - 13)
end = (today.year - 2, today.month + 8, today.day + 16)

listDji = ['AXP', 'BA', 'CAT', 'CSCO', 'VZ', 'WMT', 'XOM']
rowNum = len(listDji)
colNum = len(_quotes_historical_yahoo(listDji[0], start, end))
quotes = [[0 for col in range(64)] for row in range(rowNum)]
listTemp = [[0 for col in range(64)] for row in range(rowNum)]

for i in range(rowNum):
    quotes[i] = _quotes_historical_yahoo(listDji[i], start, end)
    for j in range(colNum-1):
        listTemp[i][j] = np.sign(np.diff(
                quotes[i], axis=0))[j][2] # 1 if the latter is larger than former, otherwise the result is -1

# print quotes[0]
# print listTemp[0][0]
# print listTemp[0]
# print len(np.sign(np.diff(quotes[i], axis=0)))

data = vstack(listTemp)
centroids, _ = kmeans(data, 4)
result, _ = vq(data, centroids)
print result
