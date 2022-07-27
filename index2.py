import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from medidas import *

app = dash.Dash(__name__, meta_tags=[
                {"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Img(src=app.get_asset_url('python_logo.jpg'),
                 id='python_logo',
                 style={
            "height": "60px",
            "width": "auto",
            "margin-bottom": "20px"
        },
        ),
    ], className=".logos_container", id="LogoPython"),
    html.Div([
        html.Img(src=app.get_asset_url('GitHub_logo.jpg'),
                 id='GitHub_logo',
                 style={
            "height": "60px",
            "width": "auto",
            "margin-bottom": "auto",                  
            },
            ),
    ], className=".logos_container", id="LogoGit"),

    html.Div([
        html.Div([
            html.H1("POBLACIÓN EN ESPAÑA", style={
                "margin-bottom": "0px", 'color': 'white', 'margin': '5px'}),
            html.H5("Python Dashboard", style={
                "margin-top": "0px", 'color': 'white'}),

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
                        )], className="row-reverse"),
        html.Div([
            html.H6(children="Mujeres : " + " " + promedio_mujeres,  # KPI titulo
                    style={
                        'textAlign': 'left',
                        'color': 'white',
                    }
                   )], className="card_container three columns")
    ]),
    html.Div([
        html.H6(children="Hombres : " + " " + promedio_hombres ,  # KPI titulo
                style={
                    'textAlign': 'left',
                    'color': 'white',
                }
               )], className="card_container three columns"),
    #FILTRO COMUNIDAD
    html.Div([
        html.Div([
            html.P('Selecciona una Comunidad:', className='fix_label',  style={'color': 'white'}),
                dcc.Dropdown(
                            df_poblacion['Comunidad'].unique(), #indicas que queres que filtre
                            id='selec_comunidad',
                            multi=False,
                            clearable=True,
                            value=Comunidad,
                            placeholder='Selecciona una Comunidad',
                            #options=[{'value': Comunidad}],
                            search_value=df_poblacion['Comunidad'].unique(),
                            className='dcc_compon'
                            )
                ])
                ])])
                
    
if __name__ == '__main__':
    app.run_server(debug=False)
