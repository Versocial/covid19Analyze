import datetime

import numpy
import pandas

startDay = 5
endDay = 30
dayNum = endDay - startDay + 1
__filePaths = [
    ('data/data.' + (datetime.datetime(2021, 12, startDay) + datetime.timedelta(days=i)).strftime('%y%m%d') + '.csv')
    for i in range(0, dayNum)]
__colors = ['red', 'darkorange', 'goldenrod', 'yellow', 'green', 'blue', 'indigo', 'gray', 'black', 'olive']

Region = 'Region'
TotalCases = 'TotalCases'
NewCases = 'NewCases'
TotalDeaths = 'TotalDeaths'
NewDeaths = 'NewDeaths'
TotalRecovered = 'TotalRecovered'
NewRecovered = 'NewRecovered'
ActiveCases = 'ActiveCases'
SeriousCases = 'SeriousCases'
CasesPerM = 'CasesPerM'
DeathsPerM = 'DeathsPerM'
TotalTests = 'TotalTests'
TestsPerM = 'TestsPerM'
Population = 'Population'

NULL = '__NULL'


def pathDay(n):
    return __filePaths[n - startDay]


__virusData = [pandas.read_csv(pathDay(i)) for i in range(startDay, endDay + 1)]


def color(n):
    return __colors[n % len(__colors)]


def dataDay(n):
    ans = __virusData[n - startDay]
    return ans


def __testX(x):
    y = NULL if str(x).isspace() or x == numpy.NAN or x is None else x
    # print('[',x,']',type(x),'[',y,']',type(y))
    return y


def cleanByLine(df):
    df = df.applymap(lambda x: __testX(x))
    df.dropna(axis=0, how='any', inplace=True)
    cols = df.columns.values.tolist()
    for col in cols:
        df = df[df[col] != NULL]
    # print(df)
    return df

def showInPercent(temp, position):
  return '%1.2f'%(temp*100) + '%'

def showInMillion(temp, position):
  return '%1.0f'%(temp/1000000) + 'M'

def showInKilo(temp, position):
  return '%1.0f'%(temp/1000) + 'k'