from pandas import Series, DataFrame

data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
        'year': [1995, 1995, 1991, 1993, 2000]}
frame = DataFrame(data)
print 'frame: \n %s' %frame
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
print 'frame: \n %s' %frame
print 'frame[\'IDE\']: \n %s' %frame['IDE']


print ('VS' in frame['IDE'])
print frame.ix[2]
