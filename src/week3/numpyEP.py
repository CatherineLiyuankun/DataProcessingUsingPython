# -*- coding: utf-8 -*-
import numpy as np

# xArray = np.ones((3,4))
# print xArray

from scipy import linalg

arr = np.array([[1, 2], [3, 4]])
print linalg.det(arr)

print np.arange(1, 10, 1).reshape(3, 3)

a = np.arange(1, 5)
print a
print np.power(a, 2)
print np.power(a, 2).sum()
print np.add(a, np.arange(4))


def fun(x, y):
    return (x + 1) * (y + 1)


arr = np.fromfunction(fun, (9, 9))
print arr


a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print a.shape
print a[[2]].sum()
print a[[2]]