import numpy as np


class PCA:
    def __init__(self, dimension, train_x):
        # 降维后的维度
        self.dimension = dimension
        # 原始数据集
        self.train_x = train_x

    @property
    def result(self):
        '返回降维后的矩阵'
        # 1. 数据中心化
        data_centering = self.train_x - np.mean(self.train_x, axis=0)
        # 2. 计算协方差矩阵
        cov_matrix = np.cov(data_centering, rowvar=False)
        # 3. 特征值分解
        eigen_val, eigen_vec = np.linalg.eig(cov_matrix)
        print(eigen_vec)
        # 4. 生成降维后的数据
        p = eigen_vec[:, 0:self.dimension]  # 取特征向量矩阵的前k维
        return np.dot(data_centering, p)


class PCA_SVD:
    def __init__(self, dimension, train_x):
        # 降维后的维度
        self.dimension = dimension
        # 原始数据集
        self.train_x = train_x

    @property
    def result(self):
        '返回降维后的矩阵'
        data_centering = self.train_x - np.mean(self.train_x, axis=0)
        # SVD
        U, Sigma, VT = np.linalg.svd(data_centering)
        # print('V==',V)
        return np.dot(data_centering, np.transpose(VT)[:, :self.dimension])
