import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

housingPrices = pd.read_csv("../Datasets/housingPrices.csv")

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

def scatterClassification(file_path, df, x_column, y_column, label_column):
    colors = ["blue", "gray", "red"]
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[i])
    
    ax.set_title("Relationship between housing area and number of rooms (Classification)")
    ax.set_xlabel("Housing area in square meters")
    ax.set_ylabel("Number of Rooms") 
    ax.legend()
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1, p_2):
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_means(points, k):
    colors = ["blue", "gray", "red"]
    DIM = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, DIM))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp, color=colors[kl])
    
    plt.title("Relationship between housing area and number of rooms (K_means)")
    plt.xlabel("Housing area in square meters")
    plt.ylabel("Number of Rooms")
    plt.savefig("Relationship Area-Rooms with K_means.png")
    plt.close()
    return mean

df = pd.DataFrame()
df['x'] = housingPrices['area_living']
df['y'] = housingPrices['n_rooms']
df['label'] = housingPrices['group']
#print(df)

scatterClassification("Relationship Area-Rooms with Classification.png", df, "x", "y", "label")

list_t = [
    (np.array(tuples[0:2]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_means(
    points,
    3,
)
print(kn)