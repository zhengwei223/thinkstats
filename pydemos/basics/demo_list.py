# coding=utf-8
'列表的用法'
l1 = [('a', 1), ('b', 2), ('c', 3)]

# 用lambda来指定参与排序的元素
l1.sort(key=lambda x: x[1], reverse=True)

print(l1)

l2 = [(9, 3, 4), (8, 1, 2), (5, 2, 3)]

"""
联合主键排序
"""
import operator

l2.sort(key=operator.itemgetter(1, 2))

print(l2)

stuinfo = {'liming': {'name': 'liming', 'score': {'yuwen': 80, 'math': 75, 'eng': 85, 'python': 60}},
           'zhangqiang': {'name': 'zhangqiang', 'age': 23, 'score': {'yuwen': 75, 'math': 89, 'eng': 78, 'python': 80}}}

print(stuinfo.items())
