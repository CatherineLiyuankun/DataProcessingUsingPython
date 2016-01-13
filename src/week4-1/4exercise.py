# -*- coding: utf-8 -*-

# 求微软公司（MSFT）2014年第一季度股票收盘价的平均值。


from matplotlib.finance import _quotes_historical_yahoo
from datetime import date
import pandas as pd

today = date.today()
start = (today.year - 2, today.month, today.day)
quotesMS = _quotes_historical_yahoo('MSFT', start, today)
attributes = ['date', 'open', 'close', 'high', 'low', 'volume']
quotesdfMS = pd.DataFrame(quotesMS, columns=attributes)
list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfMS.index = list
quotesdfMS = quotesdfMS.drop(['date'], axis=1)
list = []
quotesdfMS14 = quotesdfMS['14/01/01':'14/12/31']
for i in range(0, len(quotesdfMS14)):
    list.append(int(quotesdfMS14.index[i][3:5]))  # get month just like '02'
quotesdfMS14['month'] = list
print quotesdfMS14.groupby('month').mean().close
