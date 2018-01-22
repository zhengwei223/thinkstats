from numpy import *
import operator


def loadDataSet() -> (array, list):
    '''
    生成用于测试的数据集和分类标签
    :return:
    '''
    postingList = array([['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                         ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                         ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                         ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                         ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                         ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']])
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet: array) -> list:
    '''
    生成数据集中的词汇表
    :param dataSet:
    :return:
    '''
    vocabSet = set()
    for doc in dataSet:
        vocabSet = vocabSet | set(doc)
    return list(vocabSet)


def words2Vec(vocabList: list, wordsList: list) -> array:
    '''
    生成词汇向量表，词集模型
    :param vocabList: 全量词汇表，所有文档中的单词去重后的列表
    :param wordsList:文档，词汇集
    :return: 结果是一个向量，每个元素是1或0，意思是对应于词汇表该位置的单词是否出现在wordsSet中
    '''
    # 长度和词汇表一致
    returnVec = zeros(len(vocabList))
    for word in set(wordsList):
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1

    return returnVec


def bagOfWords2Vec(vocabList: list, wordsList: list) -> array:
    '''
    生成词汇向量表，词集模型
    :param vocabList: 全量词汇表，所有文档中的单词去重后的列表
    :param wordsList:文档，词汇集
    :return: 结果是一个向量，每个元素是1或0，意思是对应于词汇表该位置的单词是否出现在wordsSet中
    '''
    # 长度和词汇表一致
    returnVec = zeros(len(vocabList))
    for word in wordsList:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1

    return returnVec


def trainNB0(trainMatrix: array, trainCategory: list):
    '''
    朴素贝叶斯训练
    :param trainMatrix: 向量表，每行是一个样本的向量，每列是一个特征，特征为数字
    :param trainCategory: 类别列表
    :return: {类别->[特征1的条件概率，特征2的条件概率……] } ，{类别->概率}
    '''

    # 每个类别和数量的映射
    cateAndCount = dict((cate, trainCategory.count(cate)) for cate in set(trainCategory))
    # print(cateAndCount)
    # 每个分类中各特征的条件概率
    cateAndFeatureProbList = {}
    # 类别概率
    cateAndProb = {}
    # 统计每个分类中总特征数
    cateAndFeatureTotalCount = {}
    # 特征个数
    numOfFeatures = len(trainMatrix[0])
    # 初始化每个分类的特征概率分布和特征总数
    for cate in set(trainCategory):
        cateAndFeatureProbList[cate] = ones(numOfFeatures)
        cateAndFeatureTotalCount[cate] = 2.0
        # 这就是P(C_i)
        cateAndProb[cate] = cateAndCount[cate] / len(trainCategory)

    for i in range(len(trainMatrix)):
        # 这个文档所属分类
        cate = trainCategory[i]
        # 矩阵相加
        cateAndFeatureProbList[cate] += trainMatrix[i]
        # 增加所有特征的计数
        cateAndFeatureTotalCount[cate] += sum(trainMatrix[i])

    for cate in set(trainCategory):
        # 单个特征值求和除以全部特征值求和，就是在这个类别中这个特征的条件概率
        cateAndFeatureProbList[cate] = cateAndFeatureProbList[cate] / cateAndFeatureTotalCount[cate]

    return cateAndFeatureProbList, cateAndProb


def trainNB1(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords);
    p1Num = ones(numWords)  # change to ones()
    p0Denom = 2.0;
    p1Denom = 2.0  # change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)  # change to log()
    p0Vect = log(p0Num / p0Denom)  # change to log()
    printIndexAndItem("p0Vect", p0Vect)
    return p0Vect, p1Vect, pAbusive


def printIndexAndItem(msg, lst: list):
    list_ = [(w, lst[w]) for w in range(len(lst))]
    print(msg, list_)


def classifyNB(vect2classify: array, cateAndWordsProbList: dict, cateAndProb: dict):
    '''
    vect2classify属于哪个类别？
    :param vect2classify: 要进行分类的向量
    :param cateAndWordsProbList:  学习到的特征条件概率
    :param cateAndProb: 学习到的分类概率
    :return: 分类
    '''
    # 分类 -> 概率的对数
    log_probs = {}
    for cate, prob in cateAndProb.items():
        # log(连乘p(w_i|c))=Σln(p(w_i|c))
        # 词汇向量表*条件概率=待测doc的条件概率，本来应该连乘，但可能溢出，所以先求log再求和
        log_list = array(list(map(lambda x: log(x), cateAndWordsProbList[cate])))
        sumLogPwiOfC = sum(vect2classify * log_list)
        logProbOfC = log(prob)
        log_probs[cate] = sumLogPwiOfC + logProbOfC  # 这就是对数条件概率的分子了
    #     由于分母是固定的，我们只需要概率最大的那个，而不是真正要算概率

    sortedProbs = sorted(log_probs.items(), key=operator.itemgetter(1), reverse=True)
    return sortedProbs[0][0]


if __name__ == '__main__':
    postingList, classVec = loadDataSet()
    # 词汇表
    vocabList = createVocabList(postingList)
    # printIndexAndItem("vocabulary", vocabList)
    # 样本集，每行是一个样本也就是一个词汇向量，每列是一个特征，本例中是一个单词
    trainMatrix = zeros((len(postingList), len(vocabList)))
    i = 0
    for doc in postingList:
        wordsVec = words2Vec(vocabList, doc)
        trainMatrix[i, :] = wordsVec[:]
        i += 1

    cateAndWordsProbList, cateAndProb = trainNB0(trainMatrix, classVec)
    # trainNB1(trainMatrix, classVec)
    testEntry = ['dog', 'my']
    testEntry = ['you', 'are','quit','stupid']
    # 一定要转成词汇向量
    thisDoc = words2Vec(vocabList, testEntry)
    print("result", classifyNB(thisDoc, cateAndWordsProbList, cateAndProb))
