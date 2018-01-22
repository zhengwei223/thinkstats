# coding=utf-8

from math import log
import operator


def create_dataset() -> ():
    dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    feature_names = ['no surfacing', 'flippers']
    return dataset, feature_names


def calc_shannon_ent(dataset) -> float:
    '''
    计算无序香农熵：最后一列是分类标签，其实就是把类别在样本集中的频率算出来，再用-p(x)logp(x)求和计算出熵
    :param dataset: 多维矩阵
    :return: 香农熵
    '''
    # 样本总数
    entity_num = len(dataset)
    # 标签和数量的映射
    label_count_map = {}
    for feat_vec in dataset:
        _label = feat_vec[-1]
        # 把标签和出现的次数汇集到map中
        label_count_map[_label] = label_count_map.get(_label, 0) + 1
    shannon_ent = 0.0
    for _label, count in label_count_map.items():
        prob = float(count) / entity_num  # 当前标签的频率
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


def split_dataset(dataset, axis, value):
    '''
    计算sample[axis]==value的子集，并去掉sample[axis]
    :param dataset: 原数据集
    :param axis: 第axis维
    :param value: 用于过滤的值
    :return: 计算sample[axis]==value的子集，并去掉sample[axis]
    '''
    ret_dataset = []
    for feat_vect in dataset:
        if feat_vect[axis] == value:
            vect_del_axis_ = feat_vect[:axis]
            vect_del_axis_.extend(feat_vect[axis + 1:])
            ret_dataset.append(vect_del_axis_)
    return ret_dataset


def best_feature_to_split(dataset):
    '''
    确定最好的用于划分子集的特征
    :param dataset:
    :return:最好的用于划分子集的特征列的索引
    '''

    feat_num = len(dataset[0]) - 1
    # 原样本集无序熵
    base_info = calc_shannon_ent(dataset)
    best_info = 0.0
    best_feat_axis = -1
    # 迭代每一个特征向量
    for i in range(feat_num):
        # 第i列
        feat_vect = [sample[i] for sample in dataset]
        # 去重
        feat_vect_set = set(feat_vect)
        new_ent = 0.0  # 每个值过滤出的子集的熵概率之和

        for feat in feat_vect_set:
            subset = split_dataset(dataset, i, feat)
            new_ent += float(len(subset)) / len(dataset) * calc_shannon_ent(subset)
        # 当前特征作为划分，获得的信息增益
        info_gain = base_info - new_ent
        if info_gain > best_info:
            best_info = info_gain
            best_feat_axis = i
    return best_feat_axis


def major(class_list):
    '''
    从列表中选择频率最高的元素并返回
    :param class_list:
    :return:
    '''
    class_count = {(k, class_list.count(k)) for k in set(class_list)}
    sorted(class_count, key=operator.itemgetter(1), reverse=True)[0][0]


def create_tree(dataset, feature_names):
    '''
    创建决策树
    :param dataset: 原始数据集，最后一列式分类标签
    :param feature_names: 特征名称的列表
    :return: 决策树
    '''
    class_list = [sample[-1] for sample in dataset]  # 所有类标签的列表
    # 一个数据集的所有类标签都是一样的，这时这个集的所有样本都在同一个分类中
    if 1 == len(set(class_list)):
        return class_list[0]
    # 所有特征都用来划分过了，也就是现在数据集只剩下最后一列了，但是分类还有多个，那就返回频率最高的那个
    if len(dataset[0]) == 1:
        return major(class_list)
    best_feat_index = best_feature_to_split(dataset)  # 当前最好的用于划分的特征
    best_feat_label = feature_names[best_feat_index]
    mytree = {best_feat_label: {}}
    # 去掉对应的特征名称
    # del feature_names[best_feat_index]
    # 特征向量
    feat_vect = [sample[best_feat_index] for sample in dataset]
    # 去重
    feat_vect_set = set(feat_vect)
    for value in feat_vect_set:
        # 这里在递归中不要改变参数feature_names
        sub_feature_names: list = feature_names[:best_feat_index]
        sub_feature_names.extend(feature_names[best_feat_index + 1:])
        mytree[best_feat_label][value] = create_tree(split_dataset(dataset, best_feat_index, value), sub_feature_names)
    return mytree


def classify(classify_tree: dict, feature_names: list, test_vec: list):
    '''
    分类器，返回测试向量的类别字符串
    :param classify_tree: 决策树
    :param feature_names: 属性名
    :param test_vec:  测试向量
    :return: 测试向量的类别
    '''
    first_str = list(classify_tree.keys())[0]
    second_dict: dict = classify_tree[first_str]
    fea_index = feature_names.index(first_str)
    for fea_value in second_dict.keys():
        if fea_value == test_vec[fea_index]:  # 命中子节点
            if type(second_dict[fea_value]).__name__ == 'dict':
                class_name = classify(second_dict[fea_value], feature_names, test_vec)
            else:
                class_name = second_dict[fea_value]
                break
    return class_name


def storeTree(tree, fileName):
    assert isinstance(tree, dict)
    import pickle
    fw = open(fileName, 'wb+')
    pickle.dump(tree, fw)
    fw.close()


def grabTree(fileName):
    import pickle
    fr = open(fileName, 'rb+')
    return pickle.load(fr)


if __name__ == '__main__':
    dataset, feature_names = create_dataset()
    # print("shannon ent", calc_shannon_ent(dataset))
    # split_axis_0 = split_dataset(dataset, 0, 1)
    # print("split_dataset 第一个特征划分  值1", split_axis_0)
    # print("shannon ent of split_axis_0--->", calc_shannon_ent(split_axis_0))
    # split_axis_1 = split_dataset(dataset, 1, 1)
    # print("split_dataset 第2个特征划分", split_axis_1)
    # print("shannon ent of split_axis_1--->", calc_shannon_ent(split_axis_1))
    # split_axis_2 = split_dataset(dataset, 2, 'yes')
    # print("split_dataset 第3个特征划分", split_axis_2)
    # print("shannon ent of split_axis_2--->", calc_shannon_ent(split_axis_2))
    # print("the best feature used to split:", best_feature_to_split(dataset))
    #
    # print("------------------------")
    # tree = create_tree(dataset, feature_names)
    # 存储起来，二进制序列化
    # storeTree(tree, 'classifier1')
    tree: dict = grabTree('classifier1')
    res = classify(tree, feature_names, [1, 1])
    print("[1,1] result==", res)
    res = classify(tree, feature_names, [0, 1])
    print("[0,1] result==", res)
