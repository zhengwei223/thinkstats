# coding=utf-8
'字符串的一些示例'
print('this is a string')
print("this is a string")
print("""
this is a string
这样我就可以随意第换行了
哈哈
'也是一个字符串'
"双引号的字符串"
""")

# 占位符
print('my name is %s , and I\'m %s years old' % ("zhangsan", 30))

# format 元组
print('my name is {},and I\'m {} years old'.format("zhengwei", 20))

# 等价 可以调整顺序
print('my name is {1},and I\'m {0} years old'.format("zhengwei", 20))

# format2 带名称元组
print('my name is {name},and I\'m {age} years old'.format(name="zhengwei", age=20))

# format_map dict
print('my name is {name},and I\'m {age} years old'.format_map({"name": "zhengwei", "age": 20}))
