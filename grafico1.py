import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.templates
from medidas import *


#["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]
Comunidad = df_poblacion['Comunidad'].tolist()
Población = df_poblacion['Población'].tolist()
Capital   = df_poblacion['Capital'].tolist()
template = "seaborn"


fig = px.bar(
            df_poblacion,
            x=Comunidad,
            y=Población, 
            height=900, 
            width=1200, 
            color='Población',
            title="Poblacion por : '%s' Comuna" % Comunidad, #hacer un titulo dinamico segun la comunidad seleccionada
            template= template)
fig.show()



                
                


