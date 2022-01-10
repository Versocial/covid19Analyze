import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import head as h

countrys = ["China", "USA", "India", "France", "Germany",
            "UK", "Japan", "S. Korea", "Italy", "Canada"]

data = h.cleanByLine(h.dataDay(h.endDay)[[h.Region, h.TotalCases]])
data.set_index([h.Region], inplace=True)
data = data.loc[countrys]
data.sort_values(by=h.TotalCases, ascending=False, inplace=True)
fig, ax = plt.subplots()
toDraw = list(data[h.TotalCases])
print(toDraw)
ax.boxplot(toDraw, showmeans=True, meanline=True, patch_artist=True)

Y = toDraw[0:2]
Y.append(sum(toDraw) / len(toDraw))
Y.append(toDraw[len(toDraw) - 1])
TextY = ['NO.1:' + data.iloc[0].name, 'NO.2:' + data.iloc[1].name, 'Mean', 'NO.10:' + data.iloc[len(data) - 1].name]
x = 1.12
for i in range(len(Y)):
    y = Y[i]
    text = TextY[i]
    print(x, y)
    plt.text(x, y, '%.6f Million(' % (y / 1000000) + TextY[i] + ')')
plt.gca().yaxis.set_major_formatter(FuncFormatter(h.showInMillion))
plt.xticks([])
plt.xlim(0.86, 1.7)
plt.ylabel('infected number')  # y轴标注
plt.show()
