import pandas as pd
import numpy as np

dates1 = pd.date_range('20151001', periods=7)
# print dates1

dates2 = pd.DataFrame(np.random.randn(7, 3), index=dates1, columns=list('ABC'))
# print dates2
#
# print dates2.head(5)
# print dates2.tail(5)
# print dates2.index
# print dates2.columns
# print dates2[u'2015-10-16':u'2015-10-18']
# print dates2['B']
# print dates2.B

print dates2.loc[u'2015-10-01':u'2015-10-03', ['B', 'C']]
print dates2.iloc[0:3, [1, 2]]

print dates2.loc[u'2015-10-02', 'B']
print dates2.iloc[1, 1]

# print dates2.at[u'2015-10-01', 'B']
print dates2.iat[0, 1]

print dates2[(dates2.index > u'2015-10-02') & (dates2.B < 13.1)]

print dates2.mean(column=u'2015-10-02')
