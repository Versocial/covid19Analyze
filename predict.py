from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

import head as h
import scipy.stats as st

endDay = 30
startDay = 5
useEndDay = 20

worldTotalCases = [h.cleanByLine(h.dataDay(i)[[h.Region, h.TotalCases]])[h.TotalCases].sum() for i in
                   range(startDay, endDay + 1)]
worldNewCases = [int(h.cleanByLine(h.dataDay(startDay)[[h.Region, h.NewCases]])[h.NewCases].sum())]
for i in range(0, endDay - startDay):
    worldNewCases.append(worldTotalCases[i + 1] - worldTotalCases[i])

# 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
slope, intercept, r_value, p_value, std_err = st.linregress(list(range(startDay, useEndDay + 1)),
                                                            worldTotalCases[0:useEndDay - startDay + 1])

print(slope)  # 输出斜率
print(intercept)  # 输出截距
print(r_value ** 2)  # 输出 r^2

X = list(range(startDay, endDay + 1))
Y = [slope * day + intercept for day in X]
X1 = list(range(startDay, useEndDay + 1))
X2 = list(range(useEndDay + 1, endDay + 1))
Y1 = worldTotalCases[0:useEndDay - startDay + 1]
Y2 = worldTotalCases[useEndDay - startDay + 1:endDay - startDay + 1]
plt.plot(X, Y, label='predict', color='green', marker='s', ms=1)
plt.plot(X1, Y1, label='Dec.5-14', color='red', marker='s', ms=4)
plt.plot(X2, Y2, label='Dec.15-19', color='blue', marker='s', ms=4)
print(X2, Y2, worldTotalCases)
plt.title(
    'Predict day Dec.' + str(useEndDay + 1) + '-' + str(endDay) + ' by data of day Dec.' + str(startDay) + '-' + str(
        useEndDay))
plt.xticks(X)  # x轴的刻度
plt.xlim(startDay - 0.1, endDay + 0.1)  # x轴坐标范围
plt.xlabel('day in Dec.2021')  # x轴标注
plt.ylabel('new cases')  # y轴标注
plt.gca().yaxis.set_major_formatter(FuncFormatter(h.showInMillion))
plt.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0)
fig = plt.gcf()
fig.set_size_inches(9.5, 6.5, forward=True)
plt.subplots_adjust(right=0.85, left=0.085)
plt.show()
