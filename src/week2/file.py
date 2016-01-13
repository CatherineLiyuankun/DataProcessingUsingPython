# This Python file uses the following encoding: utf-8


# file_obj.write(str)将一个字符串写入文件
f = open(r'1.txt', 'w')
f.write('dkshaflkhfkla1\n2\n3\n')
f.close()

# file_obj.read(size)
#  从文件中至多读出size字节数据,返回一个字符串
# • file_obj.read()
#  读文件直到文件结束,返回一个字符串
f = open(r'1.txt')
p1 = f.read(3)
p2 = f.read()
print p1, p2
f.close()

f = open(r'1.txt')
cNames = f.readlines()
print cNames
f.close()
