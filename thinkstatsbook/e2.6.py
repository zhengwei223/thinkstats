# coding=utf-8
'''



'''
from thinkstatsbook import Pmf,survey

def prob_range(pmf,low,high):
    total=0.0
    for week in range(low,high+1):
        total+=pmf.Prob(week)
    return total

def prob_early(pmf):
    return prob_range(pmf,0,37)

def prob_on_time(pmf):
    return prob_range(pmf,38,40)

def prob_later(pmf):
    return prob_range(pmf,41,50)

def main():
    table=survey.Pregnancies()
    table.ReadRecords()
    pmf = Pmf.MakePmfFromList([getattr(x,'prglength') for x in table.records])
    early = prob_early(pmf)
    print('早生比例/概率', early)
    on_time = prob_on_time(pmf)
    print('正常比例/概率', on_time)
    later = prob_later(pmf)
    print('晚生比例/概率', later)
    print('验证概率和是否为1',early+on_time+later)

if __name__ == '__main__':
    main()