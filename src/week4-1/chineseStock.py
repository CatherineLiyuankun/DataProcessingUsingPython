# -*- coding: utf-8 -*-

# 一个中国股票数据的接口——TuShare,就可以获取上证大盘近两年的历史数据，想看什么股票直接把‘sh’改成股票代码就行了。
# http://pythonhosted.org/tushare/
import tushare as ts

print ts.get_hist_data('002738')
