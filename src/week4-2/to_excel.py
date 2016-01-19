from datetime import date
import pandas as pd
from matplotlib.finance import _quotes_historical_yahoo

today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = _quotes_historical_yahoo('IBM', start, today)
df = pd.DataFrame(quotes)
df.to_excel('stockIBM.xls', sheet_name='IBM')
