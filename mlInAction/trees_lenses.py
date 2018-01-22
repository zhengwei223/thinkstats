from mlInAction import trees

'''
佩戴隐形眼镜的各种属性的决策树
'''
if __name__ == '__main__':
    fr = open('lenses.txt', 'r')
    ds = []
    for line in fr.readlines():
        ds.append(line.split('\t'))
    names = ['age', 'prescript', 'astigmatic', 'tearRate']
    tree = trees.create_tree(ds, names)
    print(tree)
    res = trees.classify(tree, names, ['presbyopic', 'myope', 'yes', 'normal'])
    print(res)
