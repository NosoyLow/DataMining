import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

def Timestamp(position):    #   Transforma las fechas a TimeStamp de pandas
    return pd.Timestamp(position)

housingPrices = pd.read_csv("../Datasets/housingPrices.csv")
print("\n\tRegresión Lineal\n\n")
#print(housingPrices)

#   Agrupación de Fecha-Precio
datePrice = pd.DataFrame()
datePrice['date'] = housingPrices['date'].transform(Timestamp)
datePrice ['price']= housingPrices['price']
#print(datePrice) 
datePrice = datePrice.groupby(pd.Grouper(key='date', freq='2M')).mean().reset_index()
datePrice=datePrice.reset_index()
#print(datePrice)

#   Regresion Lineal

results = smf.ols('price~index', datePrice).fit()
predicts = results.predict()
#print(results.params)
print(results.summary())
bands = pd.read_html(results.summary().tables[1].as_html(),header=0,index_col=0)[0]
coef = pd.read_html(results.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
m = coef.values[1]
b = coef.values[0]
low_band = bands['[0.025'][0]
hi_band = bands['0.975]'][0]

b0 = results.params[0]
b1 = results.params[1]
datePrice['prediction'] = b0 + b1*datePrice['price']
#print(datePrice)

entrada = [[0],[len(datePrice.index)]]
lowBand = m * datePrice['index'] + low_band
highBand = m * datePrice['index'] + hi_band

meanLine = housingPrices['price'].mean()
meanLine = [[meanLine],[meanLine]]

#   Plot
plt.scatter(datePrice['index'], datePrice['price'])
plt.plot(datePrice['index'],predicts, color = 'red')
plt.plot(entrada, meanLine, color = 'green')

plt.plot(datePrice['index'], lowBand, color='orange')
plt.plot(datePrice['index'], highBand, color='orange')
plt.fill_between(datePrice['index'], lowBand, highBand, alpha=0.2, color = 'purple')

plt.title("Linear Regression Date-Price")
plt.xlabel("Date (index = bimester, Starting in 2014, Ends in 2021)")
plt.ylabel("Housing Prices Mean")
plt.savefig("Linear Regression Date-Price.png", bbox_inches="tight")
plt.close()

plt.scatter(datePrice['date'], datePrice['price'])
plt.title("Date-Price Without Linear Regression")
plt.xlabel("Date")
plt.ylabel("Housing Prices Mean")
plt.savefig("Date-Price Without Linear Regression.png", bbox_inches="tight")

