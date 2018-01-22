# coding=utf-8
'''编写两个函数， PmfMean 和 PmfVar， 两者的参数都是一个 Pmf 对象，
分别计算它的均值和方差。 看一看结果是否跟 Pmf.py 中的 Mean 和
Var 方法的结果一致'''
from thinkstatsbook import survey, thinkstats,Pmf

table = survey.Pregnancies()
table.ReadRecords()
outcome_1 = [x for x in table.records if getattr(x, 'outcome') == 1]
prglength_list = [float(getattr(x, 'prglength')) for x in outcome_1]
prglength_outcome_ord1 = [float(getattr(x, 'prglength')) for x in outcome_1 if getattr(x, 'birthord') == 1]
prglength_outcome_ord2 = [float(getattr(x, 'prglength')) for x in outcome_1 if getattr(x, 'birthord') != 1]

pmf = Pmf.MakePmfFromList(prglength_list)
pmf1 = Pmf.MakePmfFromList(prglength_outcome_ord1)
pmf2 = Pmf.MakePmfFromList(prglength_outcome_ord2)

print("全部正常生产的怀孕周均值", thinkstats.PmfMean(pmf))
print("全部正常生产的怀孕周,方差", thinkstats.PmfVar(pmf))
print("一胎怀孕周均值", thinkstats.PmfMean(pmf1))
print("一胎怀孕周方差", thinkstats.PmfVar(pmf1))
print("非一胎怀孕周均值", thinkstats.PmfMean(pmf2))
print("非一胎怀孕周方差", thinkstats.PmfVar(pmf2))
