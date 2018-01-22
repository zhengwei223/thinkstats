# coding=utf-8

from numpy import *


def loadDataSet() -> (list, list):
    dataMat = []
    labelMat = []
    fr = open('testSet_logRegress.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(x):
    return 1 / (1 + exp(-x))


def gradientAscent(dataMat, labelMat):
    '''
    梯度下降求权重向量（回归系数）
    :param dataMat: 训练集矩阵
    :param labelMat: 标签列表
    :return:
    '''
    dataMatrix = mat(dataMat)  # convert to NumPy matrix
    labelMatrix = mat(labelMat).transpose()  # convert to NumPy matrix,行向量转列向量
    # m：样本数，n：特征数
    m, n = shape(dataMatrix)
    alpha = 0.001  # 步长
    # 最多循环次数
    maxCycles = 500
    weights = ones((n, 1))  # 单位列向量，初始化各属性的权重为1
    for k in range(maxCycles):
        # 数据集乘以回归系数后进入sigmoid，结果是一个列向量
        h = sigmoid(dataMatrix * weights)  # 这就是对样本类别的预测
        # 真实值-预测值，仍是一个列向量
        error = labelMatrix - h
        # 将误差带入回归系数迭代公式 θ+= α*X.t*error
        weights += alpha * dataMatrix.transpose() * error
    return weights


def stocGradAscent0(dataMatrix, classLabels):
    '''
    随机梯度下降
    :param dataMatrix:
    :param classLabels:
    :return:
    '''
    m, n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)  # initialize to all ones，这是一个一维数组，向量
    # 遍历数据集，每次使用一个样本来更新回归系数
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weights))
        error = classLabels[i] - h
        weights += alpha * error * dataMatrix[i]
    return weights


def stocGradAscent1(dataMatrix: array, classLabels: list, numIter=150):
    '''
    改进版的随机梯度下降
    :param dataMatrix:
    :param classLabels:
    :param numIter:
    :return:
    '''
    m, n = shape(dataMatrix)
    weights = ones(n)  # initialize to all ones
    # 外层迭代次数
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.0001  # apha decreases with iteration, does not
            randIndex = int(random.uniform(0, len(dataIndex)))  # go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del (dataIndex[randIndex])  # 去除用过的随机索引
    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = [];
    ycord1 = []
    xcord2 = [];
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1]);
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]);
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1');
    plt.ylabel('X2');
    plt.show()


def classify(vect2classify: array, weights: array):
    '''
    待测向量*weights向量再求和，再用sigmoid计算，大于0.5返回1，否则返回0
    :param vect2classify:
    :param weights:
    :return:
    '''
    prob = sigmoid(sum(vect2classify * weights))
    if (prob > 0.5):
        return 1
    else:
        return 0


def colicTest(times:int):
    '''
    马疝病结果测试
    :return:
    '''

    fr_test = open('horseColicTest.txt', 'r')
    fr_train = open('horseColicTraining.txt', 'r')
    trainMat = []
    trainLabel = []
    testMatAndLabel = []
    for line in fr_train.readlines():
        line_array = [float(v) for v in line.strip().split('\t')]
        trainMat.append(line_array[:-1])
        trainLabel.append(line_array[-1])

    assert len(trainMat) == len(trainLabel)

    for line in fr_test.readlines():
        line_array = [float(v) for v in line.strip().split('\t')]
        testMatAndLabel.append(line_array)

    errorCount = 0
    for i in range(times):
        weights = stocGradAscent1(array(trainMat), trainLabel)
        for testV in testMatAndLabel:
            h = classify(testV[:-1], weights)
            if h != testV[-1]:  # 预测成功
                errorCount += 1

    print("error rate=={}".format(errorCount / times/len(testMatAndLabel)))


if __name__ == '__main__':
    colicTest(10)
    dataMat, labelMat = loadDataSet()
    # print(dataMat)
    # print(labelMat)
    # weights = gradientAscent(dataMat, labelMat)
    # print(weights)
    # plotBestFit(weights)
    weights = stocGradAscent1(array(dataMat), labelMat)
    claz = classify(array([1, -1.076637, -3.181888]), weights)
    print('claz===', claz)
