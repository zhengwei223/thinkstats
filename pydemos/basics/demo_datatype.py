# coding=utf-8
'内置数据类型'
b = '你好'
print(b)
# 长度
print(len(b.encode('gb2312')))
# 获取子序列
print(b[0:])
print(b[:1])

s = "my name is %s ,and my name is %d" % ("zheng wei".title(), 32)
print(s)

join = " ## ".join([b,s])
print(join)
