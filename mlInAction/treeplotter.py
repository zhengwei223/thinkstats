# coding=utf-8
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt: str, centerPt: tuple, parentPt: tuple, nodeType: dict):
    '''
    绘制节点
    :param nodeTxt:  节点文本
    :param centerPt: 箭头终点
    :param parentPt: 箭头起点
    :param nodeType: 节点类型
    :return:
    '''
    create_plot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt,
                             textcoords='axes fraction',
                             va='center', ha="center", bbox=nodeType, arrowprops=arrow_args)


def get_leaf_num(tree):
    '''
    获取树的叶子节点数目
    :param tree:
    :return:
    '''
    leaf_num = 0
    first_str = list(tree.keys())[0]
    second_dict = tree[first_str]
    for k in second_dict.keys():
        k_ = second_dict[k]
        if type(k_).__name__ == 'dict':
            leaf_num += get_leaf_num(k_)
        else:
            leaf_num += 1
    return leaf_num


def get_tree_depth(tree):
    '''
    获取树的深度
    :param tree:
    :return:
    '''
    max_depth = 0
    first_str = list(tree.keys())[0]
    second_dict = tree[first_str]
    for k in second_dict.keys():
        k_ = second_dict[k]
        if type(k_).__name__ == 'dict':
            this_depth = 1 + get_tree_depth(k_)
        else:
            this_depth = 1

        if this_depth > max_depth:
            max_depth = this_depth
    return max_depth


def plotTree(myTree, parentPt, nodeTxt):
    '''
    绘制一棵树
    :param myTree:
    :param parentPt: 起点坐标
    :param nodeTxt: 文字说明
    :return:
    '''
    leaf_num = get_leaf_num(myTree)
    depth = get_tree_depth(myTree)
    first_str = list(myTree.keys())[0]
    # 树的中心起点
    center_pt = (plotTree.xOff + (1.0 + float(leaf_num)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(center_pt, parentPt, nodeTxt)
    plotNode(first_str, center_pt, parentPt, decisionNode)
    second_dict = myTree[first_str]
    plotTree.yOff -= 1.0 / plotTree.totalD
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == 'dict':
            plotTree(second_dict[key], center_pt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(second_dict[key], (plotTree.xOff, plotTree.yOff), center_pt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), center_pt, str(key))

    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def plotMidText(cntrPt, parentPt, txtString):
    '''
    在父子节点中填充文本信息
    :param cntrPt:
    :param parentPt:
    :param txtString:
    :return:
    '''
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    # 绘制一个文本
    create_plot.ax1.text(xMid, yMid, txtString)


def create_plot(intree):
    # 新图形
    fig = plt.figure(1, facecolor='white')
    # 清空绘图区
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    # 全局变量
    create_plot.ax1 = plt.subplot(111, frameon=False, **axprops)

    # 绘制节点
    # plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    # 绘制节点
    # plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)


    # 树的宽度
    plotTree.totalW = float(get_leaf_num(intree))
    # 树的深度
    plotTree.totalD = float(get_tree_depth(intree))

    plotTree.xUnit = 1/plotTree.totalW
    plotTree.yUnit = 1/plotTree.totalD

    # 初始化坐标偏移量
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0

    parentPt = (0.5, 1.0)
    plotTree(intree, parentPt, '')
    plt.show()


if __name__ == '__main__':
    import mlInAction.trees as tree
    ds, fea_names = tree.create_dataset()
    intree = tree.create_tree(ds, fea_names)
    intree['no surfacing'][3] = 'maybe'
    create_plot(intree)
