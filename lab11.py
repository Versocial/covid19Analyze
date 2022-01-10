import numpy
import os

import pandas
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

import head as h

startDay = 5
endDay = 30


def worldMap(dataChoose, title, subtitle, colorMin, colorMax):
    toReplace = {
        'S. Korea': 'Korea',
        'UK': 'United Kingdom',
        'USA': 'United States',
        'Republic of the Congo': 'Dem. Rep. Congo',
        'South Sudan': 'S. Sudan',
        'Central African Republic': 'Central African Rep.',
        'Laos': 'Lao PDR'
    }
    minNumber = dataChoose.min()
    maxNumber = dataChoose.max()/1.5
    names = list(dataChoose.index)
    data = [[(toReplace[name] if name in toReplace.keys() else name), float(dataChoose[name])] for name in names]
    # names=[toReplace[name] if name in toReplace.keys() else name for name in names]
    print(maxNumber, minNumber)
    print(data)
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("World map", data, maptype="world", is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=maxNumber, min_=minNumber, range_color=[colorMin, colorMax]),
            title_opts=opts.TitleOpts(title=title,
                                      subtitle=subtitle,
                                      pos_right="center",
                                      pos_top="5%"),
        )
            .render('map.html')
    )

    print(data)


# dataChooseS = h.cleanByLine(h.dataDay(startDay)[[h.Region, h.TotalCases]]).set_index([h.Region])
# dataChooseE = h.cleanByLine(h.dataDay(endDay)[[h.Region, h.TotalCases]]).set_index([h.Region])
# dataChoose = (dataChooseE[h.TotalCases].astype(float) - dataChooseS[h.TotalCases].astype(float))
# print(dataChoose)
# population=h.cleanByLine(h.dataDay(endDay)[[h.Region,h.Population]]).set_index([h.Region]).astype(float)
# print(population)
# dataChoose=dataChoose/population[h.Population]
# print(dataChoose)
# worldMap(dataChoose, '2021.Dec 6-30 累计确诊率地图', '数据来源：https://www.worldometers.info/', '#99FF33', '#990000')
population=h.cleanByLine(h.dataDay(endDay)[[h.Region,h.Population]]).set_index([h.Region]).astype(float)
dataChoose = h.cleanByLine(h.dataDay(endDay)[[h.Region, h.TotalCases]]).set_index([h.Region])[h.TotalCases].astype(float)
dataChoose=dataChoose/population[h.Population]
worldMap(dataChoose, '2021.Dec 30 累计确诊率地图', '数据来源：https://www.worldometers.info/', '#ccff00', '#990000')
