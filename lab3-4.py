import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import head as h

data = h.cleanByLine(h.dataDay(h.endDay)[[h.Region, h.TotalCases]])
data.sort_values(by=h.TotalCases, inplace=True, ascending=False)


def lab3(n):
    title = 'infected cases Top ' + str(n) + ' (country/region)'
    dataTopN = data.iloc[0:n]
    Y = list(dataTopN[h.Region])
    Y.reverse()
    ybar = list(dataTopN[h.TotalCases])
    ybar.reverse()
    color = h.__colors
    color.reverse()
    plt.yticks(range(n), Y)
    plt.barh(range(n), ybar, height=0.7, color=color, alpha=0.8)
    plt.title(title)
    for x, y in enumerate(ybar):
        plt.text(y + 1000 * 1000, x, '%.3lf million' % ((y + 500 * 1000) / (1000 * 1000)))
    plt.subplots_adjust(left=0.115, right=0.86)
    plt.gca().xaxis.set_major_formatter(FuncFormatter(h.showInKilo))
    plt.show()


def lab4(n):
    dataTopN = data.iloc[0:n]
    dataTopN.set_index([h.Region], inplace=True)
    dataRemain = data.iloc[n:len(data)]
    print(dataTopN)
    print(dataRemain)
    toDraw = dataTopN.to_dict()[h.TotalCases]
    toDraw['Other'] = dataRemain[h.TotalCases].sum()
    print(toDraw)
    labels = list(toDraw.keys())
    size = [toDraw[label] for label in labels]
    explore = [0 for i in range(len(labels))]
    explore[len(explore) - 1] = 0.1
    patches, texts, autotexts = plt.pie(size, labels=labels, explode=explore, labeldistance=1.15,
                                        autopct="%1.1f%%", shadow=True, startangle=0, pctdistance=0.8)
    plt.savefig('lab4.png')
    plt.show()


# lab4(12)
lab3(10)
