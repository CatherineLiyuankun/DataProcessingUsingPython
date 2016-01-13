# This Python file uses the following encoding: utf-8

# import urllib
#
# r = urllib.urlopen('http://www.baidu.com/')
# html = r.read()
# print html

# Filename: dji.py 利用urllib库获取yahoo财经数据
import urllib
import re

dStr = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
m = re.findall('<tr><td class=\'yfnc_tabledata1\'><b><a href=\'.*?\'>\
(.*?)</a></b></td><td class=\'yfnc_tabledata1\'> (.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)

if m:
    print m
    print '\n'
    print len(m)
else:
    print 'not match'
