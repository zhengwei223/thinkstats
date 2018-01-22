"""
各种推导式
"""
# 列表推导式
x_ = [x * 2 for x in range(1, 11) if x & 1 == 0]
print(x_)
new_list = list(map(lambda x: x / 2, x_))
print("new List", new_list)

from functools import reduce

print("连续求和的结果", reduce(lambda x, y: x + y, new_list))

print("只要大于5的元素生成新的列表", list(filter(lambda x: x > 5, new_list)))

# 字典推导式
mca = {"a": 1, "b": 2, "c": 3, "d": 4}
print("字典推导，翻转键值", {v: k for k, v in mca.items()})

# 集合推导式
# 使用大括号，结果是一个集合，无重复元素
squared = {i * 2 for i in [1, 1, 2]}
# 如果是方括号，那么结果是一个列表，不会去重
squared = [i * 2 for i in [1, 1, 2]]
print(squared)
