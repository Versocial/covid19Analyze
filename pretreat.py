import numpy
import pandas
import os


def virusDataPretreat():
    path = "rowdata/"
    filenames = os.listdir(path)
    for file in filenames:
        rowDataPath = path + file
        rowData = pandas.read_csv(rowDataPath)
        data = rowData.applymap(lambda x: None if x == 'None' or x == 'N/A' else x)
        data.to_csv('data/' + file, index=None)


def preTreat(data):
    if data == '–':
        return None
    elif isinstance(data, str):
        toIgnore = ['*', '<', '>']
        for each in toIgnore:
            data = data.replace(each, '', -1)
    return data

def vaccDataPretreat():
    rowPath = 'vacc/vacc_row.csv'
    rowData = pandas.read_csv(rowPath)
    data = rowData.applymap(lambda x: preTreat(x))
    data.to_csv('vacc/vacc.csv')


vaccDataPretreat()
