import pandas as pd
import os

housingPrices = pd.read_csv("..\housing-prices-35.csv")
housingPricesAux = pd.DataFrame()

def get_x_position_wgs(position):
    #print (position)
    positionWP = position[7:-1]     #Remove POINT
    find = positionWP.find(' ')
    positionWP = positionWP[:find]
    #print (positionWP)
    #os.system("pause")
    return str(positionWP)

def get_y_position_wgs(position):
    #print (position)
    positionWP = position[7:-1]     #Remove POINT
    find = positionWP.find(' ')
    positionWP = positionWP[find:]
    #print (positionWP)
    #os.system("pause")
    return str(positionWP)

def get_x_lbt93(position):
    return str(position)

def get_y_lbt93(position):
    return str(position)

def remove_shape_wgs(position):
    #print(position)
    positionWP = position[15:-2]    #Remove MULTIPOLYGON((($$$$$$)))
    #print(positionWP)
    #os.system("pause")
    return str(positionWP)

housingPricesAux['x_position_wgs'] = housingPrices['position_wgs'].transform(get_x_position_wgs)
housingPricesAux['y_position_wgs'] = housingPrices['position_wgs'].transform(get_y_position_wgs)
housingPricesAux['x_lbt93'] = housingPrices['x_lbt93'].transform(get_x_lbt93)
housingPricesAux['y_lbt93'] = housingPrices['y_lbt93'].transform(get_y_lbt93)
housingPricesAux['shape_wgs'] = housingPrices['shape_wgs'].transform(remove_shape_wgs)


housingPrices = housingPrices.drop(['position_wgs','shape_wgs'], axis=1)

housingPrices.to_csv('housingPrices.csv', index = False)
housingPricesAux.to_csv('housingPricesCords.csv', index = False)

print("\n\n- - - - - Housing Prices - - - - -")
print(housingPrices.head())
print("\n\n\n\n\n- - - - - Housing Prices Cords - - - - -")
print(housingPricesAux.head())
os.system("pause")