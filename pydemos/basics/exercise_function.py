# coding=utf-8
import math


def quadratics(a, b, c):
    """
    求解一元二次方程
    ax^2+bx+c=0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项系数
    :return 两个解组成的元组或者无解
    """
    try:
        return (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a, (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    except ValueError:
        return 'no answer'


def average(*nums):
    """
    求平均值
    :param nums: 可迭代的数的集合
    :return:
    """
    return math.fsum(nums) / len(nums)


if __name__ == '__main__':
    print(quadratics(1, 2, 3))
    print(average(2, 4, 6, 8, 10))
