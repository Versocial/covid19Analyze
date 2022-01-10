import numpy

import head as h
import lab5_9 as lab


def Rate(target, base, Rate, ascending=False):
    print(h.dataDay(h.endDay))
    data = h.dataDay(h.endDay)[[h.Region, target, base]]
    data = h.cleanByLine(data)
    data[Rate] = data[target].astype(float) / data[base].astype(float)
    data.sort_values(by=Rate, inplace=True, ascending=ascending)
    return data[[h.Region, Rate]]


lab.showRateTopN(h.TotalCases, h.Population, 25, 'infected / population min 20', 'infected rate', 'country/region',
                 ascending=True)
lab.showRateTopN(h.TotalDeaths, h.TotalCases, 25, 'death / infected min 20', 'death rate', 'country/region',
                 ascending=True)
lab.showRateTopN(h.TotalDeaths, h.Population, 25, 'death / population min 20', 'death rate', 'country/region',
                 ascending=True)
