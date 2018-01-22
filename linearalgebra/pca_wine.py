# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from linearalgebra.PCA_SVD import PCA_SVD

"""
http://archive.ics.uci.edu/linearalgebra/datasets/Wine
"""


def load_data():
    '加载白酒数据'
    with open("wine.data.txt", "r") as f:
        wines = [line.strip().split(',') for line in f.readlines()]
    wines = np.array(wines, np.float)
    return wines


def draw_result(new_trainX, wines):
    """
    new_trainX:     降维后的数据
    iris:           原数据
    """
    plt.figure()
    # 提取类1
    wine1 = new_trainX[wines[:, 0] == 1]

    # 绘制点：参数1 x向量，y向量
    plt.scatter(wine1[:, 0], wine1[:, 1], color="red", label="1")

    wine2 = new_trainX[wines[:, 0] == 2]
    plt.scatter(wine2[:, 0], wine2[:, 1], color="orange", label="2")

    wine3 = new_trainX[wines[:, 0] == 3]
    plt.scatter(wine3[:, 0], wine3[:, 1], color="blue", label="3")

    plt.legend()
    plt.show()


def main(dimension=2):
    # 这是一个150*5维的矩阵
    wines = load_data()
    # 降到2维，
    pca = PCA_SVD(dimension, wines[:, 1:])

    # 降维后的数据
    _2d = pca.result
    print(_2d)
    # 降维后的数据可视化
    draw_result(_2d, wines)


if __name__ == "__main__":
    main(dimension=2)
