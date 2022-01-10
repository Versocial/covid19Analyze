import os

import pandas
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

import vaccHead as v

toReplace={
    'Mainland China':'China',
    'South Korea':'Korea',
    'U.K.':'United Kingdom',
    'Republic of the Congo':'Dem. Rep. Congo',
    'South Sudan':'S. Sudan',
    'Central African Republic':'Central African Rep.',
    'Laos':'Lao PDR'
}

dataChoose=v.cleanByLine(v.vaccData()[[v.Region,v.vaccinatedRate]])
dataChoose=dataChoose.applymap(lambda x:toReplace[x] if x in toReplace.keys() else x)
names=list(dataChoose[v.Region])
dataChoose.set_index([v.Region],inplace=True)
data=[[name,dataChoose.loc[name][v.vaccinatedRate]/100] for name in names]
print(data)
c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add("World map",data, "world",is_map_symbol_show=False, zoom=1)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=1, min_=0,range_color=[ "#330000","#66ff00"]),
        title_opts=opts.TitleOpts(title="各国疫苗接种总体情况",
                                  subtitle="统计对象：一针接种率",
                                  pos_right="center",
                                  pos_top="5%"),
    )
    .render('map.html')
)

# 打开html
# os.system("render.html")
print(data)

