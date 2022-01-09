import numpy
import pandas
import matplotlib.pyplot as plt

import head as h


def showRateTopN(target,base, n, title):
    Rate = '_Rate_'
    print(h.dataDay(h.endDay))
    data = h.dataDay(h.endDay)[[h.Region, target, base]]
    print(data)
    data=h.cleanByLine(data)
    print(data)
    data[Rate] = data[target].astype(numpy.int64) \
                 / data[base].astype(numpy.int64)
    data.sort_values(by=Rate,inplace=True,ascending=False)
    data=data.iloc[0:n]
    print(data)
    Y=list(data[h.Region])
    Y.reverse()
    ybar=list(data[Rate])
    ybar.reverse()
    color=h.__colors
    color.reverse()
    plt.yticks(range(n),Y)
    plt.barh(range(n),ybar, height=0.7, color=color, alpha=0.8)
    plt.title(title)
    for x, y in enumerate(ybar):
        plt.text(y , x , '%.3f %%' % (y*100))
    plt.subplots_adjust(left=0.2)
    plt.show()


showRateTopN(h.TotalCases,h.Population, 10, 'infected rate top 10 (country/region)')
# showRateTopN(h.TotalDeaths,h.TotalCases, 10, 'death rate top 10 (country/region)')
