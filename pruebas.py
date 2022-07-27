import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
url_Life_Expectancy = 'https://www.ine.es/jaxiT3/files/t/csv_bdsc/48882.csv'

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
#Leer
df=pd.read_csv("C://Users//melis//Documents//Melisa//Melisa Programacion//Python//Analisis Python//Poblacion//data//data.csv",error_bad_lines=False, sep=";", header=0, engine='python')
#hacer un df solo con las columnas que necesitas
df_base= df[['Provincias','Nacionalidad','Sexo','Total']] 
#df personas por genero
df_personas= df[['Provincias','Sexo','Total']] 
#eliminar una fila por un determinado contenido= 
df_personas = df_personas.drop(df_personas[df_personas['Sexo']=='Ambos sexos'].index)
df_personas = df_personas.drop(df_personas[df_personas['Provincias']=='Total Nacional'].index)

#print(df_personas.dtypes)