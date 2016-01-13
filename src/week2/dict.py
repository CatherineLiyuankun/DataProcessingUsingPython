aInfo = {'Wangdachui': 3000, 'Niuyun': 2000, 'Linling': 4500, 'Tianqi': 8000}
# info = [('Wangdachui', 3000), (['className'], 2000), ('Linling', 4500), ('Tianqi', 4500)]
info = [('Wangdachui', 3000), (123, 2000), ('Linling', 4500), ('Tianqi', ['foo', 'bar', 'baz'])]

dict1 = dict(info)
print 'dict1 %s' % dict1

dict2 = dict1.copy()
print 'dict2 %s' % dict2

dict2['Wangdachui'] = 55555
dict2['Tianqi'].remove('bar')
print 'dict1 %s' % (dict1)
print 'dict2 %s' % dict2

dict1['Linling'] = 55555
dict1['Tianqi'].append('add')
print 'dict1 %s' % (dict1)
print 'dict2 %s' % dict2



