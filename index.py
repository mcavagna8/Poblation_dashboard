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

template = "seaborn"

app = dash.Dash(__name__, meta_tags=[
                {"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Img(src=app.get_asset_url('python_logo.jpg'),
                 id='python_logo',
                 className=".logo1_container",
                ),
        html.Img(src=app.get_asset_url('GitHub_logo.jpg'),
                 id='GitHub_logo',
                 className=".logo2_container",
                ),
        ],  
        ),
    html.Div([
        html.Div([
            html.H1("POBLACIÓN EN ESPAÑA", style={"margin-bottom": "0px", 'color': 'white', 'margin': '5px'}),
            html.H5("Python Dashboard", style={"margin-top": "0px", 'color': 'white'}), 
            ], className="create_container", id="title"), ## con class name asignas el estilo de css ##
        html.Div([
            html.H6('Ultima actualizacion de Datos: ' + ' ' + str(año_max), style={'color': '#D5FCC7'}),
            ], className="three columns", 
                   id='title2', 
                   style={'float': 'right', 'position': 'right', 'top': '0 px', 'left': '0px', 'display': 'inline-block'}),
        # KPI
        html.Div([
            html.H2(["Esperanza de Vida "],
                        style={
                            'fontSize': '60',
                            'textAlign': 'left',
                            'color': 'white',
                            'position': 'flex',
                            'top': '40px',
                            'left': '60px',
                            'display': 'left',
                            'float': 'center'}
                    )
                ], className="row-reverse"),
        html.Div([
            html.H6("Mujeres : " + " " + promedio_mujeres,  # KPI titulo
                    style={
                        'textAlign': 'left',
                        'color': 'white',
                        }
                   )
                ], className="card_container three columns")
                ]
                ),
        html.Div([
            html.H6(children="Hombres : " + " " + promedio_hombres ,  # KPI titulo
                    style={
                        'textAlign': 'left',
                        'color': 'white',
                        }
                    )
                ], className="card_container three columns"),
    #FILTRO COMUNIDAD
        html.Div([
            html.H4('Selecciona una Comunidad', style="white"),
                dcc.Dropdown(
                id="dropdown",
                options= df_poblacion['Comunidad'],
                value="Comunidad",
                clearable=False
                    ),
        dcc.Graph(id="graph"),
        ]),
    #############################Graficos
        html.Div([
            html.H5('Poblacion por Comunidad', className='text-center', style= {'color':"white"}),
            dcc.Graph(id= "bar_graph", figure = {})
                ])])

#LINEAS NECESARIAS PARA INTEGRAR EL CSS CON DASH
app.css.append_css({"external_url":"C://Users//melis//Documents//Melisa//Melisa Programacion//Python//Analisis Python//Poblacion//assets//stylesheets.css"})

@app.callback(
    Output("bar_graph", "figure"), 
    Input("graph", "value"))

def update_bar_chart(value):
    
    if value == 'Comunidad': 
        fig = px.bar(
            df = df_poblacion,
            height=900, 
            width=1200, 
            title="Poblacion por : '%s' Comuna" % Comunidad, #hacer un titulo dinamico segun la comunidad seleccionada
            template = 'seaborn',  
            x='Comunidad', 
            y='Población', 
            color='Población', 
            barmode="group" )
    return fig 
###############################

if __name__ == '__main__':
    app.run_server(debug=False)
