# coding=utf-8
from numpy import *


def loadDataSet(fileName) -> (list, list):
    fr = open(fileName, 'r')
    trainSet = []
    labelList = []
    for line in fr.readlines():
        values = [float(value) for value in line.split('\t')]
        trainSet.append(values[:-1])
        labelList.append(values[-1])
    return trainSet, labelList


def selectJRand(i, m):
    '''
    在m范围内选择一个不为i的随机整数
    :param i:
    :param m:
    :return:
    '''
    j = i
    while j == i:
        j = int(random.uniform(0, m))
    return j


def clip(aj, H, L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj


def smoDimple(trainSet: list, labelList: list, C: int, maxIter: int, toler: float = 0.0):
    '''
    SMO算法的第一个版本
        创建一个alpha向量并将其初始化为0向量
        当迭代次数小于最大迭代次数时（外循环）
            对数据集中的每个数据向量（内循环）：
                如果该数据向量可以被优化：
                    随机选择另外一个数据向量
                    同时优化这两个向量
                    如果两个向量都不能被优化，退出内循环
            如果所有向量都没被优化，增加迭代数目，继续下一次循环
    max Σα-½Σα_iα_jy_iy_j<x_i,x_j>
    s.t. Σαy=0 ; α≥0
    :param C: 控制Σε的常数乘子
    :param toler:
    '''
    # 转成矩阵
    dataMatrix = mat(trainSet)
    labelColVector = mat(labelList).T  # 列向量
    m, n = shape(dataMatrix)  # 行数与列数
    b = 0
    alphas = mat(zeros((m, 1)))  # m行的列向量，全部初始化为0
    iter = 0
    # 外循环
    while iter < maxIter:
        alphaPairsChanged = 0  # 记录遍历一次数据集后被改变的alpha对
        for i in range(m):  # 开始内层循环，迭代数据集的每个样本，每个样本都有一个x，y，α
            # 阿尔法和标签做乘积(对应元素相乘)，保存在行向量中
            alpha_times_y = multiply(alphas, labelColVector).T
            # 每个x与当前x_i相乘保存在列向量中
            xj_times_xi = dataMatrix * dataMatrix[i, :].T
            # 两个向量相乘就是(Σa_jy_jx_j)·x_i,+b之后就是用当前w预测的分类数值
            wxi = alpha_times_y * xj_times_xi
            # y_i*
            yiStar = float(wxi) + b
            yi = labelList[i]
            # yi*-yi是预测与真实标签之误差
            Ei = yiStar - yi
            # if checks if an example violates KKT conditions
            # 当前的阿尔法是否违反KKT条件(αi*ci(x)==0)
            # (yi*Ei < -toler) —— 负间隔，边界之外，此时如果阿尔法小于C就违反了KKT条件
            # labelMat[i]*Ei > toler —— 正间隔，边界之外，此时如果阿尔法大于0就违反了kkt条件了
            if ((yi * Ei < -toler) and (alphas[i] < C)) or ((yi * Ei > toler) and (alphas[i] > 0)):
                # 找另一行即另一个样本
                j = selectJRand(i, m)
                # 算出y star
                yjStar = float(multiply(alphas, labelColVector).T * (dataMatrix * dataMatrix[j, :].T)) + b
                yj = labelList[j]
                Ej = yjStar - yj
                # 复制旧的α
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                # 计算L和H,它们用于将alpha[j]调整到0到C之间
                if labelList[i] != labelList[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print("L==H")
                    continue

                # Eta是alpha[j]的最优修改量2xixj-xixi-xjxj
                eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - dataMatrix[i, :] * dataMatrix[i, :].T - dataMatrix[j,:] * dataMatrix[j, :].T
                if eta >= 0:
                    print("eta>=0")
                    continue
                # 计算出一个新的alpha[j]
                # 最重要的迭代公式：a_j_new = a_j_old - y_j*(Ei-Ej)/Eta
                alphas[j] -= labelList[j] * (Ei - Ej) / eta
                alphas[j] = clip(alphas[j], H, L)  # 修剪
                # 检查alpha[j]是否有轻微改变。如果是的话，就退出for循环
                if (abs(alphas[j] - alphaJold) < 0.00001):
                    print("j not moving enough")
                    continue
                # alpha[i]和alpha[j]同样进行改变，虽然改变的大小一样，但是改变的方向正好相反（即如果一个增加，那么另外一个减少
                alphas[i] += labelList[j] * labelList[i] * (alphaJold - alphas[j])
                # 在对alpha[i]和alpha[j]进行优化之后，给这两个alpha值设置一个常数项b
                b1 = b - Ei - labelList[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[i, :].T - labelList[
                    j] * (alphas[j] - alphaJold) * dataMatrix[i, :] * dataMatrix[j, :].T
                b2 = b - Ej - labelList[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[j, :].T - labelList[
                    j] * (alphas[j] - alphaJold) * dataMatrix[j, :] * dataMatrix[j, :].T
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                '''
                在优化过程结束的同时，必须确保在合适的时机结束循环。如果程序执行到for循环的最后一行都不执行continue语句，
                那么就已经成功地改变了一对alpha，同时可以增加alphaPairsChanged的值
                '''
                alphaPairsChanged += 1
                print("iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged))
        '''
        在for循环之外，需要检查alpha值是否做了更新，如果有更新则将iter设为0后继续运行程序。
        只有在所有数据集上遍历maxIter次，且不再发生任何alpha修改之后，程序才会停止并退出while循环。
        '''
        if (alphaPairsChanged == 0):  # 遍历数据集后，没有alpha被更新
            iter += 1 # 此变量累计到maxIter，说明已经连续maxIter没有alpha被更新了
        else:
            iter = 0
    return b,alphas


if __name__ == '__main__':
    trainSet, labelList = loadDataSet('testSet_SVM.txt')
    print(len(trainSet), len(trainSet[0]), len(trainSet))
    print(labelList)
    b, alphas = smoDimple(trainSet, labelList, 0.6, 40, 0.001)
    print(b,alphas[alphas>0])
