import pandas as pd
import os

housingPrices = pd.read_csv("../Datasets/housingPrices.csv")

print("\n\tAnalisis de datos mediante Funciones de Agregación\n\n")

#print(housingPrices.head())
print("Número de filas:", len(housingPrices.index))
print("\n- - - Ventas tipo C y H más costosas - - -")
ventasC = housingPrices.groupby(["category"])[["price"]].max()
print(ventasC)

print("\n- - - Ventas tipo C y H más económicas - - -")
ventasE = housingPrices.groupby(["category"])[["price"]].min()
#ventasE = housingPrices.groupby(["category"])[["price"]].idxmin()
# print(housingPrices.loc[ventasE["price"]])
print (ventasE)

area = housingPrices['area_living'] + housingPrices['area_land']
print("\n\n- - - Media de terreno total por venta: " + str(area.mean()) + "$")
print("\n- - - Media precio de la venta: " + str(housingPrices['price'].mean()))
print("\n- - - Moda del precio de las ventas: $" + str(housingPrices['price'].mode()[0]))
print("\n- - - Dinero total transferido de las ventas: " + str(housingPrices['price'].sum()) + "$")
print("\n- - - Moda de cantidad de habitaciones: " + str(housingPrices['n_rooms'].mode()[0]))

tipos = housingPrices.groupby(["category"])['category'].count()
total = tipos[0] + tipos[1]
onePerc = 100/total 
print("\n\t- - - Conteo de tipos de ventas - - -")
print("Tipo C: {} | {:.4}%".format(tipos[0],(onePerc*tipos[0])))
print("Tipo H: {} | {:.4}%".format(tipos[1],(onePerc*tipos[1])))

print("\n\n- - - Precios de venta - - -\n")
print("Varianza: " + str(housingPrices['price'].var()))
print("Desviación estándar: " + str(housingPrices['price'].std()))
print("Curtosis: " + str(housingPrices['price'].kurtosis()) + "\n\n")
os.system("pause")