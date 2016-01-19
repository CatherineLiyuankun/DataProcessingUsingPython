# -*- coding: utf-8 -*-
#
# int 'a'; print 'b'
# a = 6
# p = 'aaa'
# list1 = []
# list1.append('q')
# list1[len(list1):] = 'a'
# print list1
# a += 3
# print
# print 'C:\file\name'
# print p + 'b'
#
# list2 = ['ccc']
# print list1+list2



def ask(prompt = "Do you like Python? ", hint = "yes or no"):
    while True:
        answer = raw_input(prompt)
        if answer.lower() in ('y', 'yes'):
            print "Thank you"
            return True
        if answer.lower() in ('n', 'no'):
            print "Why not "
            return False
        else:
            print hint


# if __name__ == '__main__':
    # ask()
    # ask("Do you like Python? ")

# print type(ask())

l = [1, 2, 3, 4]
# print l.pop();
# l.insert(2, -1);
# print l.index(3)
# l.reverse()
# print l[1]


# l = [1, 2, 3, 4, 5];
# del l[2:4];
# print l

# l = [2, 1, 3, 5, 4]; l.remove(3); l.sort();
# print l
#
# basket = ['apple', 'banana', 'apple', 'orange'] ; fruit = set(basket); print len(fruit)
#
# fruit2 = set(['apple', 'melo']); print len(fruit | fruit2)

# scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60}; del scores['Bill']; print len(scores)
scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60};
# print sorted(scores.keys())
#
s = dict(Jack=90, Mike=80, Jay=85, Bill=60);
# print scores == s
#
# for i in reversed(l):
#     print i


words = ['I', 'love', 'Python']
# for w in words:
#     if len(w) > 4:
#         words.insert(0, w)

# print words


# l = [1, 2, 3, 4, 5];
#
# for i in enumerate(l):
#      print i,'i'
#
for k, v in scores.iteritems():
    print k

# 32
# def f(x):
#      global a
#      a = 7
#      print a + x,
#
# a = 5
# f(8)
# print a

# print  (1, 2, 3, 4) < (1, 2, 4)

# import pandas
# seri = pandas.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'a'])
# print seri

#36
# print list(reversed(range(10)))[2]

#37
# a = {1, 2, 3, 4}
# b = {2, 3, 5, 6}
# print set(b) - set(a)

# #38 39
# a = [5, 1, 3, 4]
# print sorted(a, reverse = True)
# strs = ["a", "bb", "BB", "zz"]
# print sorted(strs)
#
# #40 41
# t = (1, 2.0, 'hello')
# print t == ('hello', 1, 2.0)
# print t + (3, 2)

#42-44

# def ask(prompt, hint = "yes or no", chance = 2):
#     while chance > 0:
#         answer = raw_input(prompt)
#         if answer.lower() in ('y', 'yes'):
#             print "Thank you"
#             return True
#         if answer.lower() in ('n', 'no'):
#             print "Why not "
#             return False
#         else:
#             chance -= 1
#             print hint
#     print "Sorry, you have tried too many times."
#
# ask("Do you like SciPy?")


# #45-47
# scores = [90, 80, 85, 60]
# names = ['Jack', 'Mike', 'Jay', 'Bill']
# table = dict(zip(names, scores))
# print table
# for k, v in table.items():
#   print k, '->', v

#48
# fp = open('test.txt', 'r+', 0)
# fp.readline()
# fp.seek(10, 1)
# print fp.readline()


# 定义函数sparse_vector，共有两个参数，将两个列表表示成一个稀疏向量返回，
# 并找到其中非零数值最大的下标和数值打印出来，其中第一个子列表表示该稀疏向量的下标indices,
# 例如[1, 8, 231, 500]，另一个子列表表示该稀疏向量的非零数值values, 例如[0.1, 2.3, 2.0, 10.0]
# ，输出结果为”500 10.0“。

# def sparse_vector (indices, values):
#     vector = [indices, values]
#     ind = values.index(max(values))
#     print indices[ind], values[ind]
#     return vector

# sparse_vector([1, 8, 231, 500], [0.1, 2.3, 2.0, 10.0])



