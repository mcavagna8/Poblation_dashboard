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
            "margin-bottom": "25px"},
        ),
    ])],

    html.Div([
        html.Div([
            html.H3("POBLACIÓN EN ESPAÑA", style={
                "margin-bottom": "0px", 'color': 'white', 'margin': '5px'}),
            html.H5("Python Dashboard", style={
                "margin-top": "0px", 'color': 'white'}),

        ], className="one-half column", id="title"),
        html.Div([
            html.H6('Ultima actualizacion de Datos: ' + ' ' +
                    str(año_max), style={'color': '#D5FCC7'}),

        ], className="three columns", id='title1', style={'float': 'right', 'position': 'right', 'top': '0 px', 'left': '0px', 'display': 'inline-block'}),

        # KPI
        html.Div([
            html.Hgroup(["Esperanza de Vida en España"],
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
            html.H6("Mujeres : ",  # KPI titulo
                    style={
                        'textAlign': 'left',
                        'color': 'white',
                    }
                    ),
            html.P(f"{promedio_mujeres}",
                   style={
                       'fontSize': '40',
                       'textAlign': 'left',
                       'color': '#93DAEF',
                       'position': 'static',
                       'top': '40px',
                       'left': '60px',
                       'display': 'block',
                       'float': 'center',
                   }

                   )], className="card_container three columns")

    ]),
    html.Div([
        html.H6("Hombres : ",  # KPI titulo
                style={
                    'textAlign': 'left',
                    'color': 'white',
                }
                ),
        html.P(f"{promedio_hombres}",
               style={
                   'fontSize': '30',
                   'textAlign': 'left',
                   'color': '#93DAEF',
                            'position': 'static',
                            'top': '40px',
                            'left': '60px',
                            'display': 'block',
                            'float': 'center'
               }

               )], className="card_container three columns"),

    html.Div([
        html.Div([
            html.P('Selecciona una Comunidad:', className='fix_label',
                   style={'color': 'white', 'margin-top': '2px'}),
            dcc.RadioItems(id='comunidad_radio_items',
                           labelStyle={'display': 'inline-block'},
                           options=[
                               {'Label': 'Comunidad', 'value': Comunidad},
                               {'Label': 'Población', 'value': Población}
                           ], value='Población',
                           style={'text-align': 'center', 'color': 'black'}, className='dcc_compon'),
        ], className="card_container three columns", style={'margin-botton': '20px'}),
    ], className="row flex_display")
    )
if __name__ == '__main__':
    app.run_server(debug=False)
