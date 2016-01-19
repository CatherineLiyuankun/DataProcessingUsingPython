# -*- coding: utf-8 -*-

from matplotlib.finance import _quotes_historical_yahoo
from datetime import date
import pandas as pd

today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = _quotes_historical_yahoo('IBM', start, today)
df = pd.DataFrame(quotes)
df.to_csv('stockIBM.csv')

result = pd.read_csv('stockIBM.csv')
print result