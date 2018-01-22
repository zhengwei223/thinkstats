# coding=utf-8
'''编写一个 Pumpkin 函数， 并调用 thinkstatsbook.py 中的函数计算上一节中
南瓜重量的均值、 方差和标准差。
假如我在花园里种了一些蔬菜， 到了收获的时
候， 我收获了三个装饰用的南瓜， 每个 1 磅重； 两个制南瓜饼的南
瓜， 每个 3 磅重； 还有一个重达 591 磅的大西洋巨型南瓜
'''
from thinkstatsbook import thinkstats, survey


def Pumpkin():
    t = (1, 1, 1, 3, 3, 591)
    mean = thinkstats.Mean(t)
    print("均值", mean)
    var = thinkstats.Var(t)
    print('方差', var)
    print('标准差', var ** 0.5)
    return


table = survey.Pregnancies()
table.ReadRecords()

# 计算均值方差等
def Pregnance():
    outcome_1 = [x for x in table.records if getattr(x, 'outcome') == 1]
    prglength_outcome_ord1 = [float(getattr(x, 'prglength')) for x in outcome_1 if getattr(x, 'birthord') == 1]
    prglength_outcome_ord2 = [float(getattr(x, 'prglength')) for x in outcome_1 if getattr(x, 'birthord') != 1]

    prglength_list = [float(getattr(x, 'prglength')) for x in outcome_1]
    mean = thinkstats.Mean(prglength_list)
    print("全部正常生产的怀孕周均值", mean)
    print("全部正常生产的怀孕周,方差", thinkstats.Var(prglength_list))
    print("一胎怀孕周均值", thinkstats.Mean(prglength_outcome_ord1))
    print("一胎怀孕周方差", thinkstats.Var(prglength_outcome_ord1))
    print("非一胎怀孕周均值", thinkstats.Mean(prglength_outcome_ord2))
    print("非一胎怀孕周方差", thinkstats.Var(prglength_outcome_ord2))

    return


'画图咯'
from matplotlib import pyplot
from thinkstatsbook import Pmf


def DrawHist():
    '绘制孕周统计直方图'
    # 孕周列表
    prglength_list = [float(getattr(x, 'prglength')) for x in table.records]
    # 直方图对象
    hist = Pmf.MakeHistFromList(prglength_list)

    # orderdMode = sorted(hist.Items(), key=lambda x: x[1], reverse=True)
    # print("众数", orderdMode)
    # 提取值和频数
    vals, freqs = hist.Render()
    # 调用pyplot来绘制直方图
    pyplot.bar(vals, freqs)
    pyplot.show()


# possible mass function
def DrawPMF():
    '绘制概率质量函数'
    # 孕周列表
    prglength_list = [float(getattr(x, 'prglength')) for x in table.records]
    # 直方图对象
    pmf = Pmf.MakePmfFromList(prglength_list)

    vals, p = pmf.Render()
    # 调用pyplot来绘制直方图
    pyplot.bar(vals, p)
    pyplot.plot(vals, p)
    pyplot.show()


if __name__ == '__main__':
    # Pumpkin()
    Pregnance()
    # DrawHist()
    # DrawPMF()
