import datetime

import numpy
import pandas
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


def color(n):
    return ['red', 'darkorange', 'goldenrod', 'yellow', 'green', 'blue', 'indigo', 'gray', 'black', 'olive'][n % 10]


def path(n):
    return \
    [('rowdata/data.' + (datetime.datetime(2021, 12, 5) + datetime.timedelta(days=i)).strftime('%y%m%d') + '.csv')
     for i in range(0, 15)][n]


def TotalCasesIncTop10():
    data0 = pandas.read_csv(path(0))[['Region', 'TotalCases']]
    data0.rename(columns={'TotalCases': 'TotalCases0'}, inplace=True)
    data14 = pandas.read_csv(path(14))[['Region', 'TotalCases']]
    data14.rename(columns={'TotalCases': 'TotalCases14'}, inplace=True)
    joinData = pandas.merge(left=data0, right=data14, how='inner', left_on='Region', right_on='Region')
    print(joinData)
    joinData['TotalCasesInc'] = joinData['TotalCases14'] - joinData['TotalCases0']
    joinData.sort_values(by='TotalCasesInc', ascending=False, inplace=True)
    print(joinData)
    return joinData


def PrintTotalCasesIncTop10():
    data = TotalCasesIncTop10().head(10)
    data.replace(to_replace='None', value=None,
                 inplace=True)  # lambda x:x if(isinstance(int)or(isinstance(str)and not x=='None'))else None,inplace=True
    for i in range(0, 15):
        dataI = pandas.read_csv(path(i))
        dataI.replace(to_replace='None', value=None, inplace=True)
        dataI.rename(columns={'NewCases': 'NewCases' + str(i)}, inplace=True)
        data = pandas.merge(left=data, right=dataI, how='left', left_on='Region', right_on='Region')
        pandas.set_option('display.max_columns', None)
    print(data)
    for i in range(0, 10):
        region = data.iloc[i]['Region']
        print(region)
        X = [i for i in (range(0 + 5, 15 + 5))]
        choose = numpy.isfinite(
            data[data['Region'] == region][['NewCases' + str(i) for i in range(0, 15)]].astype(numpy.double))
        Y = \
        data[data['Region'] == region][['NewCases' + str(i) for i in range(0, 15)]][choose].astype(numpy.double).iloc[
            0].tolist()
        print(Y)
        plt.plot(X, Y,
                 label='NO.' + str(i + 1) + region,
                 color=color(i))
    plt.rcParams['savefig.dpi'] = 180
    plt.rcParams['figure.dpi'] = 180
    plt.subplots_adjust(right=0.7)
    plt.title('Total Cases Top 10 From 2021-12-5 to 2021-12-19')
    plt.legend(bbox_to_anchor=(1.03, 0), loc=3, borderaxespad=0)
    plt.show()


if __name__ == '__main__':
    TotalCasesIncTop10()
    PrintTotalCasesIncTop10()
