'''
字典的使用

'''

a = {'a': 'value1', 'b': 'value2', 'c': 'value3'}
print(a)

# 迭代键
for x in a.keys():
    print(x)
# 迭代元组
for x in a.items():
    print(x)
# 键排序
key_list = list(a.keys())
key_list.sort()
# 排序后输出键值
for x in key_list:
    print(x, a[x])
