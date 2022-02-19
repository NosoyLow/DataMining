import os
import shutil

os.environ['KAGGLE_USERNAME'] = 'nosoylow'
os.environ['KAGGLE_KEY'] = '557d28036eea28030cfc8e63cb85638a'

from kaggle.api.kaggle_api_extended import KaggleApi

dataset = 'cheneblanc/housing-prices-35-fr'
path = 'datasets'

print ("\n\n\nA continuación se descargará el archivo 'housing-prices-35.csv' del usuario @cheneblanc\n")
os.system("pause")

api = KaggleApi()
api.authenticate()

api.dataset_download_files(dataset, path)

shutil.unpack_archive('datasets/housing-prices-35-fr.zip', path)
os.remove("datasets/housing-prices-35-fr.zip")
print ("\nArchivo descargado\n")