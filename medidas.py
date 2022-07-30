from turtle import color
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from matplotlib import pyplot as plt
import plotly.graph_objs as go
import pandas as pd

#DF expectativa de vida URL
#Ruta
url_Life_Expectancy = 'https://www.ine.es/jaxiT3/files/t/csv_bdsc/48882.csv'
#Creo el df
df_Life_Expectancy = pd.read_csv(
    url_Life_Expectancy, error_bad_lines=False, sep=";", header=0, engine='python')

# crear el df mujeres para despues filtrar
mujeres_max = df_Life_Expectancy[df_Life_Expectancy["Sexo"] == "Mujeres"]

# filtrar el ultimo registro
mujeres_max = df_Life_Expectancy[df_Life_Expectancy["Sexo"] == "Mujeres"].head(1)
mujeres_min = df_Life_Expectancy[df_Life_Expectancy["Sexo"] == "Mujeres"].tail(1)
hombres_max = df_Life_Expectancy[df_Life_Expectancy["Sexo"] == "Hombres"].head(1)
hombres_min = df_Life_Expectancy[df_Life_Expectancy["Sexo"] == "Hombres"].tail(1)

#filtrar el numero edad promedio por mujeres
promedio_mujeres= mujeres_max.iloc[0]['Total']
promedio_hombres= hombres_max.iloc[0]['Total']

# filtrar año maximo
año_max = df_Life_Expectancy["Periodo"].iloc[0]

##################################################################################
#df poblacion
df_poblacion = pd.read_csv("C://Users//melis//Documents//Melisa//Melisa Programacion//Python//Analisis Python//Poblacion//data//data_spain.txt", 
error_bad_lines=False, sep=",", header=0, engine='python')
#Mapa 

colors =['#E8EAE3', '#B6DED9', '#F1B0AE', '#FEDEDC', '#B5EFE8']
background = '#0000ff'

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
cmap = plt.colormaps['RdGy']

Comunidad = df_poblacion['Comunidad'].tolist()
Población = df_poblacion['Población'].tolist()
Capital   = df_poblacion['Capital'].tolist()

color_graf = ['orange', '#dd1e35', 'green', '#e55467']
