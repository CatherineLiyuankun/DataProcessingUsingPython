# -*- coding: utf-8 -*-
# 50 计算MovieLens 100k数据集中男性女性用户评分的标准差并输出。
#
# 数据集下载http://files.grouplens.org/datasets/movielens/ml-100k.zip
#
# 其中u.data 表示100k条评分记录，每一列的数值含义是：
#
# user id | item id | rating | timestamp
#
# u.user表示用户的信息，每一列的数值含义是：
#
# user id | age | gender | occupation | zip code
#
# u.item文件表示电影的相关信息，每一列的数值含义是：
#
# movie id | movie title | release date | video release date |IMDb URL | unknown | Action |
#  Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir |
#  Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |
#
# 可能会用到的相关函数：
#
# pandas.read_table(filepath_or_buffer, sep='\t', names=None)
#
# pandas.pivot_table(data, values=None, columns=None, aggfunc='mean')
#
# pandas.merge(left, right, how='inner')
#
# 更详尽的API文档请参考http://pandas.pydata.org/pandas-docs/stable/ 。
# 程序运行结果：
#
# gender
# F         *.*(只是示意)
# M         *.*(只是示意)
# Name: rating, dtype: float64

# http://blog.csdn.net/chenghit/article/details/50352954
# 1使用pandas.read_table() 读出u.data和u.user，生成2个DataFrame read_table API Reference
# 2使用 pandas.merge()把2个df作多对一的合并，把’user id’，’rating’，’gender’合进一个DataFrame。
# 实际上只需要用这几个列，其它列都不需要。u.item也不需要 merge API Reference
# 3使用pandas.pivot_table()生成数据透视表，同时集中计算每个用户的评分均值。pivot_table API Reference Pandas透视表（pivot_table）详解
# 4使用std() 计算Female和Male的评分标准差
# 5print输出

import pandas as pd
import numpy as np

data_fields = ['user id', 'item id', 'rating', 'timestamp']
user_fields = ['user id', 'age', 'gender', 'occupation', 'zip code']

# 默认names = None，此时pd.read_table会拿第1行的value当作列名
data_df = pd.read_table(r"./ml-100k/u.data", names=data_fields)
# 默认sep = '\t'，拿tab作为分列符
user_df = pd.read_table(r"./ml-100k/u.user", sep="|", names=user_fields)
# 生成2个新的DataFrame,去掉不需要的列
data1_df = pd.DataFrame([])
data1_df['user id'] = data_df['user id']
data1_df['rating'] = data_df['rating']
user1_df = pd.DataFrame([])
user1_df['user id'] = user_df['user id']
user1_df['gender'] = user_df['gender']
# 合并2个DataFrame, 默认how = 'inner'，即新的DF仅包含2个DF交集的Key
rating_df = pd.merge(data1_df, user1_df)
# 按性别生成数据透视表, 默认aggfunc = 'mean', 即values是每个用户为N个电影打分的平均值
# 注意：pivot_table的类型不是DataFrame, 而是Series, 所以要进行转换
gender_s = pd.pivot_table(rating_df, index=['gender', 'user id'],
                          values='rating')
gender_df = pd.DataFrame(gender_s)
# 对DataFrame进行筛选，分别生成女性和男性的DataFrame
Female_df = gender_df.query("gender == ['F']")
Male_df = gender_df.query("gender == ['M']")
# 按性别计算评分标准差
Female_std = np.std(Female_df)
Male_std = np.std(Male_df)
# 格式化输出
print 'Gender\n', 'F\t%.6f' % Female_std, '\nM\t%.6f' % Male_std
