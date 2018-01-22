# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from linearalgebra.PCA_SVD import PCA_SVD

"""
该数据有150个样本，每个样本有4个属性，一个目标（即分类结果）。

现在我们希望在一个平面（二维空间）里面把这些样本以点的形式来展现，且将不同类的点标为不同的颜色，用以观察聚合与分散程度。
"""


def load_iris_data():
    '加载鸢尾花数据'
    with open("iris.data.txt", "r") as f:
        iris = []
        for line in f.readlines():
            temp = line.strip().split(",")
            # 将分类转为数字
            if temp[4] == "Iris-setosa":
                temp[4] = 0
            elif temp[4] == "Iris-versicolor":
                temp[4] = 1
            elif temp[4] == "Iris-virginica":
                temp[4] = 2
            else:
                raise (Exception("data error."))
            iris.append(temp)
    iris = np.array(iris, np.float)
    return iris


def draw_result(new_trainX, iris):
    """
    new_trainX:     降维后的数据
    iris:           原数据
    """
    plt.figure()
    # 提取Iris-setosa
    setosa = new_trainX[iris[:, 4] == 0]

    # 绘制点：参数1 x向量，y向量
    plt.scatter(setosa[:, 0], setosa[:, 1], color="red", label="Iris-setosa")

    # Iris-versicolor
    versicolor = new_trainX[iris[:, 4] == 1]
    plt.scatter(versicolor[:, 0], versicolor[:, 1], color="orange", label="Iris-versicolor")

    # Iris-virginica
    virginica = new_trainX[iris[:, 4] == 2]
    plt.scatter(virginica[:, 0], virginica[:, 1], color="blue", label="Iris-virginica")
    plt.legend()
    plt.show()


def main(dimension=2):
    # 这是一个150*5维的矩阵
    iris = load_iris_data()
    # 降到2维，
    pca = PCA_SVD(dimension, iris[:, :4])

    # 降维后的数据
    iris_2d = pca.result

    # 降维后的数据可视化
    draw_result(iris_2d, iris)


if __name__ == "__main__":
    main(dimension=2)
