"""
函数
"""


# coding=utf-8

def fib(n):
    "函数示例：斐波那契数列"
    if n == 1 or n == 2:
        return 1
    if n <= 0:
        return 0

    a1 = 1
    a2 = 1
    for x in range(2, n + 1):
        res = a1 + a2
        a1 = a2
        a2 = res
    return res


for x in range(1, 10):
    print(fib(x))

print(fib.__doc__)


def test1(a,b=4):
    "示意默认参数的使用，默认参数必须放在非默认参数的后面，调用时传值是可选的"
    return a+b;

print(test1(a=10))