# This Python file uses the following encoding: utf-8

# 将文件1.txt 的字符串前加上序号1、2、3、...后写到 另一个文件s1.txt中。

# f1 = open(r'1.txt')
# cNames = f1.readlines()
# for i in range(0, len(cNames)):
#     cNames[i] = str(i + 1) + ' ' + cNames[i]
# f1.close()
#
# f2 = open(r's1.txt', 'w')
# f2.writelines(cNames)
# f2.close()


# file_obj.seek(offset , whence=0)
# − 在文件中移动文件指针,从 whence(0表示文件头部,1表示 当前位置,2表示文件尾部)偏 移offset个字节
# – whence参数可选,默认值为0

s = 'Tencent Technology Company Limited'
f = open(r'1.txt', 'a+')
f.writelines('\n')
f.writelines(s)
f.seek(0, 0)
cNames = f.readlines()
print cNames
f.close()
