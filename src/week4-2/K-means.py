# -*- coding: utf-8 -*-
from pylab import *
from scipy.cluster.vq import *

list1 = [88, 74, 96, 85]
list2 = [92, 99, 95, 94]
list3 = [91, 87, 99, 95]
list4 = [78, 99, 97, 81]
list5 = [88, 78, 98, 84]
list6 = [100, 95, 100, 92]
data = vstack((list1, list2, list3, list4, list5, list6))
data = data.astype('float')
centroids, _ = kmeans(data, 2)
result, _ = vq(data, centroids)
print result
