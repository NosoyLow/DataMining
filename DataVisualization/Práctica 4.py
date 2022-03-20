import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

housingPrices = pd.read_csv("../Datasets/housingPrices.csv")

print("\n\tVisualización de Datos\n\n")
#print(housingPrices.head())

#   Graph of Category of sales
types = ['C', 'H']
ch = housingPrices.groupby(["category"])['category'].count()
typesCount = [ch[0], ch[1]]

fig, [ax1, ax2] = plt.subplots(1,2)
ax1.bar(types, typesCount)
ax1.set_ylabel('Number of Sales')
ax2.pie(housingPrices.groupby(["category"])['category'].count(), labels = ['Category C', 'Category H'],autopct="%0.1f %%")
fig.suptitle("Category of sales")
fig.legend(['Category C - ' + str(ch[0]), 'Category H - ' + str(ch[1])])
fig.savefig("Category of sales.png")
plt.close()

#   Graph of Number of Rooms by Sales
fig, [ax1, ax2] = plt.subplots(1,2)
ax1.title.set_text("Histogram")
ax1.hist(housingPrices["n_rooms"])
ax1.set_xlabel('Number of Rooms')
ax1.set_ylabel('Sales Counter')
ax2.boxplot(housingPrices["n_rooms"])
ax2.title.set_text("Boxplot")
ax2.set_xlabel('Number of Rooms')
ax2.xaxis.set_major_locator(plt.NullLocator())
fig.suptitle("Number of Rooms by Sales\n")
fig.savefig("Number of Rooms by Sales.png")
plt.close()

#   Graph of Sales in Ille-et-Vilaine 
fig, [ax1, ax2] = plt.subplots(1,2)
ax1.scatter(housingPrices['x_lbt93'], housingPrices['y_lbt93'])
ax2 = plt.imshow(mpimg.imread('Ille-et-Vilaine.jpg'))
ax2.axes.xaxis.set_visible(False)
ax2.axes.yaxis.set_visible(False)
fig.suptitle("Sales in Ille-et-Vilaine - Coordinates are in lbt93")
fig.savefig("Sales in Ille-et-Vilaine.png")
plt.close()

#   Graph of Relationship between housing area and number of rooms
plt.scatter(housingPrices['area_living'], housingPrices['n_rooms'])
plt.title("Relationship between housing area and number of rooms")
plt.xlabel("housing area in square meters")
plt.ylabel("Number of Rooms")
plt.savefig("Relationship Area-Rooms.png")
plt.close()

#   Graph of Price of Sales
fig, [ax1, ax2] = plt.subplots(1,2)
ax1.boxplot(housingPrices['price'], sym='')
ax2.boxplot(housingPrices['price'])
fig.suptitle("Price of Sales (y-axis = price)")
ax1.title.set_text("Boxplot without outliers")
ax2.title.set_text("Boxplot")
ax1.xaxis.set_major_locator(plt.NullLocator())
ax2.xaxis.set_major_locator(plt.NullLocator())
fig.savefig("Price of Sales.png")
plt.close()

print("Gráficas generadas correctamente")
os.system("pause")