import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

housingPrices = pd.read_csv("../Datasets/housingPrices.csv")

print("\n\tPruebas Estadísticas\n\n")
#print(housingPrices.head())

C = housingPrices[housingPrices['category'] == 'C']
H = housingPrices[housingPrices['category'] == 'H']

print("Partimos realizando una prueba de normalidad de el área de vivienda que tienen las ventas\n")
print("Para esto realizamos los estadísiticos de asimertría y curtosis los cuales pueden emplearese para detectar desviaciones de la normalidad")
print("Un valor de curtosis y/o coeficiente de asimetría entre -1 y 1, es generalmente considerada una ligera desviación de la normalidad")
print("Entre -2 y 2 hay una evidente desviación de la normal pero no extrema.")
print("\nRealizamos una curtosis al area de vivienda por venta")
print("\tCondominios: " + str(stats.kurtosis(C['area_living'])))
print("\tCasas: " + str(stats.kurtosis(H['area_living'])))

print("\nRealizamos una asimetría al area de vivienda por venta")

print("\tCondominios: " + str(stats.skew(C['area_living'])))
print("\tCasas: " + str(stats.skew(H['area_living'])))

print("\n- - - Con estos datos podemos concluir que el area de vivienda por casa no mantiene una distribución normal- - -\n\n")

fig, [ax1, ax2] = plt.subplots(1,2)
ax1.violinplot(C['area_living'])
ax2.violinplot(H['area_living'])
fig.suptitle("Distribuciones del area de vivienda de las ventas")
ax1.set_xlabel('Condominios')
ax2.set_xlabel('Casas')
fig.savefig("Distribución de áreas de vivienda.png")
plt.close()

print("Al no ser distribuciones normales, tenemos que aplicar una prueba no paramétrica.")
print("En este caso utilizaremos la prueba no paramétrica de suma de rango de Wilcoxon, ya que nuestros datos son poblaciones independientes.")
print ("Como nuestra población es de 97mil datos, generamos una muestra pequeña eliminando aleatoriamente columnas")

print("\nEn este caso se quiere comprobar si las distribuciones son idénticas, intervalo de confianza = 95%")

np.random.seed(14)
drop_indices = np.random.choice(H.index, 17398, replace=False)
H = H.drop(drop_indices)
drop_indices = np.random.choice(H.index, 39650, replace=False)
H = H.drop(drop_indices)
drop_indices = np.random.choice(C.index, 39650, replace=False)
C = C.drop(drop_indices)

alfa = 0.05/2
stat, pvalue = stats.wilcoxon(C['area_living'], H['area_living'])

print("\nComo -> " + str(pvalue) + " > " + str(alfa) + " o " + str(pvalue) + " < " + str(alfa))
if (pvalue > alfa or pvalue < alfa):   
    print("\nSe rechaza la hipótesis, por lo tanto, son diferentes las distribuciones de las categorías de las ventas\n\n")
else:
    print("\nSe acepta la hipótesis, por lo tanto, son iguales las distribuciones de las categorías de las ventas\n\n")

os.system("pause")