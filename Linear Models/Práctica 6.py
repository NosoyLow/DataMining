from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import os

model = LinearRegression()
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
print(datePrice)


#   Regresion Lineal

regresion = LinearRegression()

low = datePrice['index'].values.reshape((-1,1))
modelo = regresion.fit(low, datePrice['price'])
#print("b = ", modelo.intercept_)
#print("m = ", modelo.coef_)
entrada = [[0],[50]]
#print(modelo.predict(entrada))
#print(housingPrices['price'].mean())
meanLine = housingPrices['price'].mean()
meanLine = [[meanLine],[meanLine]]


#   Plot
plt.scatter(datePrice['index'], datePrice['price'])
plt.plot(entrada, modelo.predict(entrada), color = 'red')
plt.plot(entrada, meanLine, color = 'green')

plt.title("Linear Regression Date-Price")
plt.xlabel("Date (index = bimester, Starting in 2014, Ends in 2021)")
plt.ylabel("House Prices Mean")
#plt.xticks(datePrice['index'].to_numpy(), datePrice['date'].to_numpy())
#plt.xticks(rotation=90)
plt.savefig("Linear Regression Date-Price.png", bbox_inches="tight")
plt.close()

plt.scatter(datePrice['date'], datePrice['price'])
plt.title("Date-Price Without Linear Regression")
plt.xlabel("Date")
plt.ylabel("House Prices Mean")
plt.savefig("Date-Price Without Linear Regression.png", bbox_inches="tight")
