import numpy
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

import vaccHead as v
import head as h

toRepalce = {
    'Mainland China': 'China',
    'South Korea': 'S. Korea',
    'U.K.': 'UK',
    'United States': 'USA',
}

def Rate(target, base, Rate, ascending=False):
    data = h.dataDay(h.endDay)[[h.Region, target, base]]
    data = h.cleanByLine(data)
    data[Rate] = data[target].astype(float) / data[base].astype(float)
    data.sort_values(by=Rate, inplace=True, ascending=ascending)
    return data[[h.Region, Rate]]


deathPerPerson = 'deathByPopulation'
deathPerInfected = 'deathByInfected'
infectedPerPerson = 'infectedByPopulation'
deathByPopulation = Rate(h.TotalDeaths, h.Population, deathPerPerson)
deathByInfected = Rate(h.TotalDeaths, h.TotalCases, deathPerInfected)
infectedByPopulation = Rate(h.TotalCases, h.Population, infectedPerPerson)

n = 10
data = v.cleanByLine(v.vaccData()[[v.Region, v.DoesPer100]])
vaccRate = 'vaccRate'
data[vaccRate] = data[v.DoesPer100] / 100
vaccByPopulation = data[[v.Region, vaccRate]]

vaccByPopulation= vaccByPopulation.applymap(lambda x: toRepalce[x] if x in toRepalce.keys() else x)
deathByPopulation.set_index([h.Region], inplace=True)
deathByInfected.set_index([h.Region], inplace=True)
infectedByPopulation.set_index([h.Region], inplace=True)
vaccByPopulation.set_index([v.Region], inplace=True)
deathByPopulationMax=deathByPopulation[deathPerPerson].max()
deathByInfectedMax=deathByInfected[deathPerInfected].max()
infectedByPopulationMax=infectedByPopulation[infectedPerPerson].max()
vaccByPopulationMax=vaccByPopulation[vaccRate].max()

PointsGot = (deathByInfectedMax - deathByInfected[deathPerInfected]) /deathByInfectedMax\
            * (deathByPopulationMax - deathByPopulation[deathPerPerson]) /deathByPopulationMax\
            * (infectedByPopulationMax - infectedByPopulation[infectedPerPerson])/infectedByPopulationMax\
            * (infectedByPopulationMax - infectedByPopulation[infectedPerPerson])/infectedByPopulationMax\
            * vaccByPopulation[vaccRate]/vaccByPopulationMax * 100

n=10
PointsGot.sort_values(inplace=True, ascending=False)
print(PointsGot.iloc[0:n])
Top10=list(PointsGot.iloc[0:n])
countrys=list(PointsGot.iloc[0:n].index)
countrys.reverse()
Top10.reverse()
color=h.__colors
color.reverse()
plt.xticks(list(range(0,100,10)))
plt.yticks(range(n),countrys )
plt.barh(range(n), Top10, height=0.7, color=color, alpha=0.8)
plt.title('Epidemic prevention score Top 10')
for x, y in enumerate(Top10):
    plt.text(y, x, ' %.3lf' % y)
plt.xlabel('points')
plt.ylabel('country/region')
fig = plt.gcf()
fig.set_size_inches(9.5, 6.5, forward=True)
plt.show()