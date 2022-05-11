import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

housingPrices = pd.read_csv("../Datasets/housingPrices.csv")

 #   Formula de distancia entre dos puntos, como el eje 'y' es muy pequeño, redondeamos a el rango de 'x'
def ClassificationFunc(position):   
    radioA = 150
    radioB = 250

    distancia = np.sqrt( housingPrices['area_living'][position]**2 + housingPrices['n_rooms'][position]**2 )
    
    if distancia <= radioA:
        return "Grupo A"
    elif distancia <= radioB and distancia > radioA:
        return "Grupo B"
    elif  distancia > radioB:
        return "Grupo C"
    
    return "GrupoC"

#   Grafica sin clasificación
plt.scatter(housingPrices['area_living'], housingPrices['n_rooms'])
plt.title("Relationship between housing area and number of rooms")
plt.xlabel("Housing area in square meters")
plt.ylabel("Number of Rooms")
plt.savefig("Relationship Area-Rooms.png")
plt.close()

housingPrices=housingPrices.reset_index()
housingPrices['group'] = housingPrices['index'].transform(ClassificationFunc)
#print(housingPrices)

#   Grafica con clasificación
def scatterClassification(file_path, df, x_column, y_column, label_column):
    colors = ["blue", "gray", "red"]
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[i])
    
    ax.set_title("Relationship between housing area and number of rooms")
    ax.set_xlabel("Housing area in square meters")
    ax.set_ylabel("Number of Rooms") 
    ax.legend()
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1, p_2) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

scatterClassification("Relationship Area-Rooms with Classification", housingPrices, "area_living", "n_rooms", "group")

df = pd.DataFrame()
df['x'] = housingPrices['area_living']
df['y'] = housingPrices['n_rooms']
df['label'] = housingPrices['group']
#print(df)

list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]

points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(
    points,
    labels,
    [np.array([5, 100]), np.array([8, 200]), np.array([10, 300]), np.array([12, 400])],
    5,
)
print(kn)