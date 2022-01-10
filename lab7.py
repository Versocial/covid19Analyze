from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

import vaccHead as v

n = 10
data = v.cleanByLine(v.vaccData()[[v.Region, v.DoesPer100]])
Rate = '__Rate'
data[Rate] = data[v.DoesPer100] / 100
data.sort_values(by=Rate, inplace=True)
data = data.iloc[0:n]
title = ''

Y = list(data[v.Region])
Y.reverse()
ybar = list(data[Rate])
ybar.reverse()
color = v.__colors
color.reverse()
plt.yticks(range(n), Y)
plt.barh(range(n), ybar, height=0.7, color=color, alpha=0.8)
plt.title(title)
for x, y in enumerate(ybar):
    plt.text(y, x, ' %.1f%%' % (y * 100))
plt.subplots_adjust(left=0.2)
plt.gca().xaxis.set_major_formatter(FuncFormatter(v.showInPercent))
plt.xlabel('vaccinated rate')  # x轴标注
plt.ylabel('country/region')  # y轴标注
plt.show()
