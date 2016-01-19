# -*- coding: utf-8 -*-
from matplotlib.finance import _quotes_historical_yahoo
import pandas as pd
from datetime import date
from datetime import datetime

today = date.today()
start = datetime(2014, 1, 1)
end = datetime(2014, 12, 31)
quotesMS14 = _quotes_historical_yahoo('MSFT', start, end)
attributes = ['date', 'open', 'close', 'high', 'low', 'volume']
quotesdfMS14 = pd.DataFrame(quotesMS14, columns=attributes)

# 为这部分数据将索引列更换为日期，并删除掉原先的date列，日期格式是2015年1月30日，显示为 ‘15/01/30’
list1 = []
for i in range(0, len(quotesMS14)):
    x = date.fromordinal(int(quotesMS14[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list1.append(y)
quotesdfMS14.index = list1
quotesdfMS14 = quotesdfMS14.drop(['date'], axis=1)

# 加上月份列
list1 = []
for i in range(0, len(quotesdfMS14)):
    list1.append(int(quotesdfMS14.index[i][3:5]))
quotesdfMS14['month'] = list1
# print quotesdfMS14


# 绘制在2014年整年内（即1月1日至12月31日）微软股票每个月开盘平均价格的走势。

import matplotlib.pyplot as plt

openMS = quotesdfMS14.groupby('month').mean().open
print openMS
listopen = []
for i in range(1, 13):
    listopen.append(openMS[i])

plt.plot(openMS.index, listopen)
# plt.bar(openMS.index, listopen, 'r-.*')
# plt.bar(openMS.index, openMS.values)
plt.plot(openMS.index, openMS.values, '-.*r')
plt.plot(openMS.index, listopen, 'rs')

# 增加标题，要求增加标题‘Stock Statistics of Microsoft in 2014’，增加横坐标‘Month’，增加纵坐标‘Average Open Price’ 。请填写第一个空格处的答案。

plt.plot(openMS.index, listopen)
plt.xlabel('Month')
plt.ylabel('Average Open Price')
plt.title(' Stock Statistics of Microsoft')

# 利用pandas绘制在2014年整年内（即1月1日至12月31日）微软股票每个月开盘平均价格的走势
openMS.plot()

plt.plot(openMS.index, openMS.values)

# 通过命令____type(openMS)____可以得到（答案中出现的字符请都用小写表示）openMS对象类型是pandas.core.series.Series，
# plt.plot 实际上是库matplotlib的方法，其后跟的参数openMS.index和openMS.values分别代表绘制图表时的x轴和y轴。
# 而openMS.plot() 实际上是调用了库 __pandas__ 的自带方法。
# 可以看到matplotlib作为基础库，在不优化默认的情况下所绘制出来的图案不如_pandas___库优化的展示结果。
print type(openMS)

# 添加如下代码，得到INTEL公司2014年一整年的股票开盘价折线图
quotesINT = _quotes_historical_yahoo('INTC', start, end)
quotesdfINT = pd.DataFrame(quotesINT, columns=attributes)
list = []
for i in range(0, len(quotesINT)):
    x = date.fromordinal(int(quotesINT[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfINT.index = list
quotesdfINT = quotesdfINT.drop(['date'], axis=1)
list = []
quotesdfINT14 = quotesdfINT['14/01/01':'15/01/01']
print quotesdfINT14
quotesdfINT14.open.plot()

# 添加如下代码，用折线图比较Microsoft和Intel在2014年一整年的股票开盘价走势。

compdf = pd.DataFrame()
compdf['MS'] = quotesdfMS14.open
compdf['INTEL'] = quotesdfINT14.open
compdf.plot(title='open price of MS and INTEL')

# 散布图（Scatter plot）是观察两个一维数据序列之间关系的有效手段，
# 请填写空格以得到微软在2014整年中每日收盘价与开盘价之差与当日成交量之间的散布图（数据在前几题的基础上）。

plt.scatter(quotesdfMS14.close - quotesdfMS14.open, quotesdfMS14.volume)
