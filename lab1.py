from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

import head as h

endDay=30
startDay=5

worldTotalCases=[ h.cleanByLine(h.dataDay(i)[[h.Region,h.TotalCases]])[h.TotalCases].sum() for i in range(startDay,endDay+1) ]
worldNewCases=[int(h.cleanByLine(h.dataDay(startDay)[[h.Region,h.NewCases]])[h.NewCases].sum())]
for i in range(0,endDay-startDay):
    worldNewCases.append(worldTotalCases[i+1]-worldTotalCases[i])
print('sdf',worldNewCases)

day=list(range(startDay,endDay+1))
plt.plot(day, worldNewCases,lw=1, c='red', marker='s', ms=4)
fig = plt.gcf()
fig.set_size_inches(9.5, 6.5, forward=True)
plt.rcParams['savefig.dpi'] = 180
plt.rcParams['figure.dpi'] = 180
plt.subplots_adjust(right=0.99,left=0.07)
plt.title('New Cases From 2021-12-'+str(startDay)+' to 2021-12-'+str(endDay))
plt.xticks(day)  # x轴的刻度
plt.xlim(startDay-0.5, endDay+0.5)  # x轴坐标范围
plt.gca().yaxis.set_major_formatter(FuncFormatter(h.showInKilo))
plt.xlabel('day in Dec.2021')  # x轴标注
plt.ylabel('cases number')  # y轴标注
plt.show()
