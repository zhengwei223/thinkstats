import sys
a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' % a
d = "中文编程"
e = a
c = b
b2 = a.replace("中", "中")

print(sys.getrefcount('中文编程'))
