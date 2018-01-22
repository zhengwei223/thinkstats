# coding=utf-8
"""
语句和数据结构的综合练习

"""

"""
print(2),
print(4),

t = open('1.txt', 'w')
# 修改标准输出的定向
sys.stdout = t
print(str('第一行'.encode('utf-8')))
print(str('第二行'.encode('utf-8')))
t.close();

# 改回控制台重定向
sys.stdout = sys.__stdout__
x = 2
if x > 2:
    print('x >2')
else:
    print('x<=2')
"""

"""
将成绩转换为级别
"""


def score2level():
    score = int(input("请输入一个分数："))

    if score > 90:
        print("优秀")
    elif score > 80:
        print("良好")
    elif score > 60:
        print("及格")
    else:
        print("不及格")


def num2list():
    """输出一个数字的每个位上的数"""
    num_str = input("请输入一个数字：")
    num_len = len(num_str)
    num = int(num_str)
    # 除数,**是指数运算
    divisor = 10 ** (num_len - 1)
    res = []
    while divisor != 0:
        # 注意要进行int转换，python中两数相除结果默认是浮点型
        res.append(int(num / divisor))
        num = num % divisor
        divisor = int(divisor / 10)

    return res


def exercise1():
    a = "aAsmr3idd4bgs7Dlsf9eAF"
    # 1.1---大小写转换
    print("1.1:", a.swapcase())
    # 1.2 提取所有的数字并输出
    print('1.2:', ''.join([x for x in a if x.isdigit()]))
    # 1.3 输出字符串中每个字符在该串中出现的次数
    print('1.3:', dict([(x, a.count(x)) for x in set(a)]))

    # 1.4 去掉重复字符，并按原顺序输出新字符串
    set_list = list(set(list(a)))  # 去重
    # 排序前，先将每个键用a.index运算一下，再论大小
    set_list.sort(key=a.index)  # 恢复原顺序
    print('1.4:', ''.join(set_list))

    # 1.5 逆序输出字符串
    print('1.5:', a[:: -1])  # 如此简洁，-1是步长

    # 1.6 去数字后对字母排序，但是要求同样的字母出现在一起且大写在前
    letter_list = [x for x in a if x.isalpha()]

    """方法一
        letter_upper_list = [x for x in letter_list if x.isupper()]
        letter_lower_list = [x for x in letter_list if x.islower()]
        letter_lower_list.sort()
        letter_upper_list.sort()
        for x in letter_upper_list:
            x_index = letter_lower_list.index(x.lower())
            if x_index >= 0:  # 存在对应的小写字母
    """
    '''方法二'''
    # key是用来处理列表元素的函数
    print('1.6:', sorted(letter_list, key=str.lower))

    # 1.7 判断单词boy中的字符是否全部出现在字符串a当中
    search = 'boy'
    a_set = set(a)
    a_set.update(list(search))  # 将目标列表中的元素依次添加到set中
    # 比较添加操作过后的长度，如果都存在，长度应该是不会变化的，因为set不允许重复
    print('1.7:', len(set(a)) == len(a_set))

    # 1.8 判断这些单词的字符是否全部出现在字符串a当中
    word_list = ['boy', 'girl', 'bird', 'dirty']
    a_set = set(a)
    for x in word_list:
        a_set.update(list(x))

    print("1.8:", len(set(a)) == len(a_set))

    # 根据字符的频率统计，按频率由高到低输出字符和次数
    count_list = [(x, a.count(x)) for x in set(a)]
    count_list.sort(key=lambda x: x[1], reverse=True)
    print('1.9:', count_list)


import os

'''
获得import this 命令的提示文本
统计该文本中be is than这三个单词出现的次数
'''


def exercise2():
    content = os.popen('python -m this').read()
    content = content.replace('\n', '')
    # 转列表
    word_list = content.split(' ')
    res = [(x, word_list.count(x)) for x in ['be', 'is', 'than']]
    print(res)


# 将数字列表中的数字取出拼接成字符串
def exercise3():
    a = [1, 2, 3, 6, 8, 9, 10, 14, 17]
    s = str(a)[1:-1].replace(', ', '')
    print(s)


print("exe1:")
exercise1()

print("exe2:")
exercise2()

print("exe3:")
exercise3()
