import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import head as h


def showRateTopN(target, base, n, title, xlabel, ylabel, ascending=False):
    Rate = '_Rate_'
    print(h.dataDay(h.endDay))
    data = h.dataDay(h.endDay)[[h.Region, target, base]]
    print(data)
    data = h.cleanByLine(data)
    print(data)
    data[Rate] = data[target].astype(numpy.int64) \
                 / data[base].astype(numpy.int64)
    data.sort_values(by=Rate, inplace=True, ascending=ascending)
    data = data.iloc[0:n]
    print(data)
    Y = list(data[h.Region])
    Y.reverse()
    ybar = list(data[Rate])
    ybar.reverse()
    color = h.__colors
    color.reverse()
    plt.yticks(range(n), Y)
    plt.barh(range(n), ybar, height=0.7, color=color, alpha=0.8)
    plt.title(title)
    for x, y in enumerate(ybar):
        plt.text(y, x, ' %.2f %%' % (y * 100))
    plt.subplots_adjust(left=0.23, right=0.92)
    plt.gca().xaxis.set_major_formatter(FuncFormatter(h.showInPercent))
    plt.xlabel(xlabel)  # x轴标注
    plt.ylabel(ylabel)  # y轴标注
    plt.show()

# showRateTopN(h.TotalCases, h.Population, 10, 'infected rate top 10 (country/region)','infected rate','country/region')
# showRateTopN(h.TotalDeaths,h.TotalCases, 10, 'death rate top 10 (country/region)','death rate','country/region')
