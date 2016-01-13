from pandas import Series

# aSer = Series([1, 2.0, 'a'])
# print aSer
#
# bSer = Series(['apple', 'peach', 'lemon'], index=[1, 2, 3])
# print bSer
#
# print bSer.index
# print bSer.values


# data = {'AXP': '86.40', 'CSCO': '122.64', 'BA': '99.44'}
# sindex = ['AXP', 'CSCO', 'BA', 'AAPL']
# aSer = Series(data, index=sindex)
# print aSer
#
# print Series.isnull(aSer)
#
# bSer = {'AXP': '86.40', 'CSCO': '122.64', 'CVX': '23.78'}
# cSer = Series(bSer)
# print cSer
# print aSer + cSer


sa = Series(['a', 'b', 'c'], index = [0, 1, 2])
sb = Series(['a', 'b', 'c'])
sc = Series(['a', 'c', 'b'])
print sa.equals(sc)
print sb.equals(sa)
print sa*3 + sc*2
