import pandas
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

import head as h

startDay=5
endDay=19

def TopN(n):
    TotalCasesBefore='TotalCases0'
    TotalCasesInc='TotalCasesInc'
    datas=h.dataDay(startDay)[[h.Region,h.TotalCases,h.NewCases]]
    datas=h.cleanByLine(datas)
    datas[TotalCasesBefore]=datas[h.TotalCases]-datas[h.NewCases]
    datas=h.cleanByLine(datas[[h.Region,TotalCasesBefore]])
    datae=h.dataDay(endDay)[[h.Region,h.TotalCases]]
    joinData=pandas.merge(left=datas, right=datae, how='inner', left_on=h.Region, right_on=h.Region)
    joinData=h.cleanByLine(joinData)
    joinData[TotalCasesInc]=joinData[h.TotalCases]-joinData[TotalCasesBefore]
    joinData.sort_values(by=TotalCasesInc,inplace=True,ascending=False)
    joinData=joinData.iloc[0:n]
    return joinData[h.Region]

n=10
countrys= list(TopN(n))
days=list(range(startDay,endDay+1))
for i in range(n):
    country=countrys[i]
    dataStart=h.cleanByLine(h.dataDay(startDay)[[h.Region, h.NewCases]])
    dataStart.set_index([h.Region], inplace=True)
    data=[int(dataStart.loc[country][h.NewCases])]

    dataDays = []
    for j in range(startDay, endDay + 1):
        dataDay = h.cleanByLine(h.dataDay(j)[[h.Region, h.TotalCases]])
        dataDay.set_index([h.Region], inplace=True)
        dataDays.append(dataDay.loc[country][h.TotalCases])
    print('||',country,dataDays)
    for j in range(endDay-startDay):
        data.append(dataDays[j+1]-dataDays[j])
    plt.plot(days, data,lw=1, c=h.color(i), marker=None, ms=4,label='NO.'+str(i+1)+':\n'+country)

fig = plt.gcf()
fig.set_size_inches(9.5, 6.5, forward=True)

plt.rcParams['savefig.dpi'] = 180
plt.rcParams['figure.dpi'] = 180
plt.subplots_adjust(right=0.82,left=0.075)
plt.title('New Cases From 2021-12-'+str(startDay)+' to 2021-12-'+str(endDay))
plt.xticks(days)  # x轴的刻度
plt.xlim(startDay-0.1, endDay+0.1)  # x轴坐标范围
plt.xlabel('day in Dec.2021')  # x轴标注
plt.ylabel('new cases')  # y轴标注
plt.gca().yaxis.set_major_formatter(FuncFormatter(h.showInKilo))
plt.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0)
plt.show()




