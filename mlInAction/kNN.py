# coding=utf-8
from numpy import *
import matplotlib.pyplot as plot
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    '''
    :param inX: 待预测数据
    :param dataSet: 训练集
    :param labels:  训练集的标签
    :param k: 前k个邻近
    :return: 预测的分类
    '''
    dataSetSize = dataSet.shape[0]  # 样本数
    inData = tile(inX, (dataSetSize, 1))  # 将向量或矩阵inX扩展，第二个参数（x,y）:x垂直扩展，y水平扩展
    # print("tile",inData)
    diffMat = inData - dataSet  # 矩阵相减，每个向量是新数据和样本点的特征分量的差
    sqDiffMat = diffMat ** 2  # 距离矩阵的平方，矩阵每个点独自平方
    # print("sqDiffMat", sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)  # 一维求和，每个值就是新数据和样本的距离的平方
    # print("sqDistances", sqDistances)
    distances = sqDistances ** 0.5  # 开方
    sortedDistIndicies = distances.argsort()  # 排序
    # print("sortedDistIndicies", sortedDistIndicies)

    # 标签和数量的映射
    classCount = {}
    # 取前k个
    for i in range(k):
        # 这是第I个标签
        voteILabel = labels[sortedDistIndicies[i]]  # 标签按排序罗列
        # 出现一次，计数加1
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1  # 以标签为键，计数
    # 按标签在前k中出现的次数排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2Matrix(fileName):
    fr = open(fileName, 'r')
    readlines = fr.readlines()
    numOflines = len(readlines)
    returnMatrix = zeros((numOflines, 3))
    labelVector = []
    index = 0
    for line in readlines:
        line = line.strip()
        lineItems = line.split("\t")
        returnMatrix[index, :] = lineItems[:3]
        labelVector.append(lineItems[-1])
        index += 1
    return returnMatrix, labelVector


def label2Num(x):
    if x == "largeDoses":
        return 50
    if x == "smallDoses":
        return 20
    if x == "didntLike":
        return 10


def label2Color(x):
    if x == "largeDoses":
        return 'r'
    if x == "smallDoses":
        return 'b'
    if x == "didntLike":
        return 'g'


def showScatterFigure(data, labels):
    fig = plot.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 0], s=list(map(label2Num, labels)), c=list(map(label2Color, labels)))
    # ax.scatter(data[:, 1], data[:, 2], 15.0 * array(labels), 15.0 * array(labels))
    plot.ylabel('Percentage of Time Spent Playing Video Games')
    plot.xlabel('常旅客里程')

    plot.show()


def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 从列中选取最小值
    maxVals = dataSet.max(0)  # 从列中选取最大值

    # print(minVals,maxVals)

    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    # 减去所在列的最小值
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 除以range
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest(k):
    hoRatio = 0.1
    datingDataMat, datingLabels = file2Matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        res = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], k)
        print("真实标签为{}，计算结果为{}，{}".format(datingLabels[i], res, res == datingLabels[i]))
        if datingLabels[i] != res:
            errorCount += 1.0
    print("error rate is", errorCount / float(numTestVecs))


if __name__ == '__main__':
    # group, labels = createDataSet()
    # print(group)
    # print(labels)

    # claz = classify0([0.5, .5], group, labels, 2)
    # print(claz)

    data, labels = file2Matrix('datingTestSet.txt')
    # print(set(labels))
    normDataSet, ranges, minVals = autoNorm(data)
    # print(normDataSet)
    # showScatterFigure(normDataSet, labels)

    # datingClassTest(10)
    percentTats = float(input("玩视频游戏的视频比例："))
    ffMiles = float(input("每年赢得的里程："))
    iceCream = float(input("每年消费冰淇淋："))
    inX = (array([percentTats, ffMiles, iceCream]) - minVals) / ranges
    claz = classify0(inX, normDataSet, labels, 5)
    print(claz)
