# -*- coding: utf-8 -*-

# from matplotlib.finance import quotes_historical_yahoo
# matplotlib 1.5版本中函数变为 quotes_historical_yahoo_ohlc 或 _quotes_historical_yahoo

from matplotlib.finance import _quotes_historical_yahoo
from datetime import date
from datetime import datetime
import pandas as pd

today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = _quotes_historical_yahoo('AXP', start, today)
# print quotes
fields = ['date', 'open', 'close', 'high', 'low', 'volume']

list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x, '%Y-%m-%d')
    list1.append(y)


quotesdf = pd.DataFrame(quotes, index=list1, columns=fields)
quotesdf = quotesdf.drop(['date'], axis=1)
quotesdf.close.plot()

# quotesdf = pd.DataFrame(quotes, index=range(1, len(quotes) + 1), columns=fields)


print quotesdf

# from matplotlib.finance import quotes_historical_yahoo_ochl
# from datetime import date, timedelta
# import pandas as pd
# today = date.today()
# start = today - timedelta(days=365)
# quotes = quotes_historical_yahoo_ochl('GOOG', start, today)
# quotesdf = pd.DataFrame(quotes)
# print quotesdf
