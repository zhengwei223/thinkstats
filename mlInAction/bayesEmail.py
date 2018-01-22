# coding=utf-8
from numpy import *
import operator
import re
from os import listdir
import random
from mlInAction import bayes


def text2wordList(bigString) -> list:
    listOfTokens = re.compile(r'\W*').split(bigString)
    return [word.lower() for word in listOfTokens if len(word) > 2]


def spamTest(dir1: str, dir2: str, time: int):
    '''
    测试分类器效果
    :param dir1: 正常邮件所在目录
    :param dir2: 垃圾邮件所在目录
    :return:
    '''
    docList = []
    classList = []
    fileList = listdir(dir1)
    # ------构造doclist begin--------
    # 对于正常邮件
    for fileName in fileList:
        bigStr = open(dir1 + "/" + fileName).read()
        # print(fileName)
        wordList = text2wordList(bigStr)
        docList.append(wordList)
        classList.append(0)
    # 对于垃圾邮件
    fileList = listdir(dir2)
    for fileName in fileList:
        bigStr = open(dir2 + "/" + fileName).read()
        # print(fileName)
        wordList = text2wordList(bigStr)
        docList.append(wordList)
        classList.append(1)
    # ------构造doclist end--------

    vocabList = bayes.createVocabList(docList)

    errorRateSum = 0.0
    for count in range(time):
        _docList = []
        _classList = []
        _docList[:] = docList[:]
        _classList[:] = classList[:]
        # 选择一部分出来作为训练集，10个样本作为测试，其余作为训练集
        trainSet = []
        testSet = []
        testClassList = []
        for i in range(10):
            # 随机整数 0-全集size
            randIndex = int(random.uniform(0, len(_docList)))
            testSet.append(_docList[randIndex])
            testClassList.append(_classList[randIndex])
            del _docList[randIndex]
            del _classList[randIndex]

        # 用训练集构建向量矩阵
        trainMat = []
        for doc in _docList:
            trainMat.append(bayes.bagOfWords2Vec(vocabList, doc))

        # 训练出单词的条件概率和类别的概率分布
        cateAndWordsProbList, cateAndProb = bayes.trainNB0(trainMat, _classList)

        index = 0
        rightCount = 0
        errorCount = 0
        testTotalNum = len(testSet)
        for doc in testSet:
            wordVector = bayes.bagOfWords2Vec(vocabList, doc)
            claz = bayes.classifyNB(wordVector, cateAndWordsProbList, cateAndProb)
            # 预测正确
            if claz == testClassList[index]:
                rightCount += 1
            else:
                errorCount += 1
            index += 1

        rate = errorCount / testTotalNum
        print("交叉验证第{}次，错误率{}".format(count, rate))
        errorRateSum += rate
    return errorRateSum / time


if __name__ == '__main__':
    errorRate = spamTest("email/ham", "email/spam", 10)
    print('total error rate is {}'.format(errorRate))
