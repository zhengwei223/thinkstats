from matplotlib import pyplot

from thinkstatsbook import survey, Pmf


def prob_of_week(pmf, week):
    cond_pmf = pmf.Copy()
    for v in pmf.Values():
        if v < week:
            cond_pmf.Remove(v)
    cond_pmf.Normalize()
    return 'week%d' % week, cond_pmf.Prob(week)


def main():
    table = survey.Pregnancies()
    table.ReadRecords()
    # 概率密度函数
    probs1, weeks1 = weeks_prods(table, lambda x: getattr(x, 'birthord') == 1)
    pyplot.plot(weeks1, probs1, label='first babies')

    probs2, weeks2 = weeks_prods(table, lambda x: getattr(x, 'birthord') != 1)
    pyplot.plot(weeks2, probs2, label='other babies')
    pyplot.savefig('概率对比图.pdf', format='pdf', dpi=300)
    pyplot.show()
    # Brewer.ClearIter()
    pyplot.clf()

def weeks_prods(table, _filter):
    pmf_ord1 = Pmf.MakePmfFromList([getattr(x, 'prglength') for x in table.records if _filter(x)])
    weeks = []
    probs = []
    for week in range(35, 46):
        name, prob = prob_of_week(pmf_ord1, week)
        # print('1胎', name,prob)
        weeks.append(week)
        probs.append(prob)
    return probs, weeks


if __name__ == '__main__':
    main()
