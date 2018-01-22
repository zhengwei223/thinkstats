# coding=utf-8
from numpy import *
from mlInAction import kNN
from os import listdir


def img2vector(filename):
    vect = zeros((1, 1024))
    f = open(filename, 'r')
    for i in range(32):
        line = f.readline()
        for j in range(32):
            vect[0, 32 * i + j] = line[j]
    return vect


def handWritingClassTest():
    training_data_set,training_labels=loadData("trainingDigits")
    test_data_set,test_labels=loadData("testDigits")
    # print(set(training_labels))
    print("len(test_data_set)",len(test_data_set))
    test_data_count = len(test_data_set)
    error_count=0
    for i in range(test_data_count):
        res=kNN.classify0(test_data_set[i],training_data_set,training_labels,5)
        if res!=test_labels[i]:
            error_count+=1

    print("error count is {}".format(error_count))
    print("total test count is {}".format(test_data_count))
    print("error rate is {}".format(error_count/test_data_count))


def loadData(dir):
    file_list = listdir(dir)
    labels = []
    file_list=list(filter(lambda x:not x.startswith(r'.'),file_list))
    data_set = zeros((len(file_list), 1024))
    index = 0
    for file_name in file_list:
        digit = file_name.split("_")[0]
        if digit==r'.':
            continue
        labels.append(int(digit))
        data_set[index] = img2vector("trainingDigits/" + file_name)
        index += 1
    return data_set,labels

if __name__ == '__main__':
    # vector = img2vector("trainingDigits/0_0.txt")
    # print(len(vector[0]))
    handWritingClassTest()
