# -*- coding: utf-8 -*-
from matplotlib.finance import _quotes_historical_yahoo
from datetime import date
import pandas as pd

# 使得获取到的数据是从两年前的今天到现在的微软公司的股票历史数据（关于微软的公司代号，可以在该页面http://finance.yahoo.com/q/cp?s=^DJI 中找到）
today = date.today()
start = (today.year - 2, today.month, today.day)
quotes = _quotes_historical_yahoo('MSFT', start, today)

# 为微软的quotes数据添加属性名:
attributes = ['date', 'open', 'close', 'high', 'low', 'volume']
quotesdf = pd.DataFrame(quotes, columns=attributes)

# 为这部分数据将索引列更换为日期，并删除掉原先的date列，日期格式是2015年1月30日，显示为 ‘15/01/30’
list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list1.append(y)
quotesdf.index = list1
quotesdf = quotesdf.drop(['date'], axis=1)

# 获取2014年1月30日到2月10日这期间微软更换CEO阶段股票的开盘价和收盘价
quotesdf.ix['14/01/30':'14/02/10', ['open', 'close']]

# 查询在2014年下半年（即6月1日至12月31日）微软股票收盘价大于49美元的记录
quotesdf['14/06/01':'14/12/31'][quotesdf.close > 49]

# 查询在2014年整年内（即1月1日至12月31日）微软股票收盘价最高的5天数据
print quotesdf['14/01/01':'14/12/31'].sort('close', ascending=False)[0:5]

# 可以得到根据成交量升序排列的2014年上半年的微软股票数据
quotesdf['14/01/01':'14/05/31'].sort('volume')

# 统计在2014年整年内（即1月1日至12月31日）微软股票涨价的每个月天数据
list1 = []
tmpdf = quotesdf['14/01/01':'14/12/31']
for i in range(0, len(tmpdf)):
    list1.append(int(tmpdf.index[i][3:5]))
tmpdf['month'] = list1
tmpdf[tmpdf.close > tmpdf.open]['month'].value_counts()

# 统计在2014年整年内（即1月1日至12月31日）微软股票每个月的总成交量。
tmpdf.groupby('month')['volume'].sum()

# 合并在2014年整年内（即1月1日至12月31日）微软股票收盘价最高的5天和最低的5天。请填写第一个空格处的答案。
sorted = quotesdf.sort('close')
pd.concat([sorted[:5], sorted[-5:]])

# print quotesdf
