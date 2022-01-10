import numpy
import pandas

Region = 'Region'
vaccinatedRate = 'vaccinatedRate'
fullyVaccinatedRate = 'fullyVaccinatedRate'
AdditionalDoesRate = 'AdditionalDoesRate'
DoesPer100 = 'DoesPer100'
AdditionalDoes = 'AdditionalDoes'
TotalDoes = 'TotalDoes'

__vaccData = pandas.read_csv('vacc/vacc.csv')

__colors = ['red', 'darkorange', 'goldenrod', 'yellow', 'green', 'blue', 'indigo', 'gray', 'black', 'olive']

def vaccData():
    data = __vaccData
    data=data.applymap(lambda x: float(x[0:len(x) - 1]) if isinstance(x, str) and x[len(x) - 1] == '%' else x)

    return data.iloc[2:len(data)]


NULL = '__NULL'


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
    return df

def showInPercent(temp, position):
  return '%1.2f'%(temp*100) + '%'


def showInKilo(temp, position):
  return '%1.0f'%(temp/1000) + 'k'