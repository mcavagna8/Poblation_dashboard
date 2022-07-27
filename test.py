import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

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


app = dash.Dash(__name__, meta_tags=[
                {"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('python_logo.jpg'),
                id='python_logo',
                style= 
                {
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px"
                         
                },
                    ),
        html.Div([
            html.Div([
                html.H3("POBLACIÓN EN ESPAÑA", style={ "margin-bottom": "0px", 'color': 'white', 'margin': '5px'}),                       
                html.H5("Python Dashboard",style={"margin-top": "0px", 'color': 'white'}),
            
        ], className="one-half column", id="title"),
        html.Div([
                html.H6('Ultima actualizacion de Datos: ' + ' ' + str(año_max), style={'color': '#D5FCC7'}), 

                ], className="three columns", id='title1',style={'float': 'right','position': 'right','top': '0 px','left':'0px','display': 'inline-block'}),
        
        #####KPI
        html.Div([
                html.H6("Edad Promedio : ",#####KPI titulo
                        style={
                            'textAlign': 'center',
                            'color': 'white',
                            'position': 'static',
                            'top': '40px',
                            'left': '60px',
                            'display': 'block',
                            'float':'inline-start'
                            }
                        ),
                html.H6(" Mujeres : ",#####KPI titulo
                        style={
                            'textAlign': 'center',
                            'color': 'white',
                            'position': 'static',
                            'top': '40px',
                            'left': '60px',
                            'display': 'block',
                            'float':'left'
                            }
                        ),        
                html.P(f"{(promedio_mujeres)}",
                        style={
                            'fontSize': '30',
                            'textAlign':'center',
                            'color': '#FF8675',
                            'position': 'static',
                            'top': '40px',
                            'left': '60px',
                            'display': 'block',
                            'float':'left'                            }
                        ),
        html.Div([
                html.H6("Hombres : ",#####KPI titulo
                        style={
                            'textAlign': 'center',
                            'color': 'white',
                            'position': 'static',
                            'top': '40px',
                            'left': '60px',
                            'display': 'inline',
                            'float':'left' 
                            }
                        ),
                        
                html.P(f"{promedio_hombres}",
                        style={
                            'fontSize': '30',
                            'textAlign':'center',
                            'color': '#93DAEF',
                            'position': 'static',
                            'top': '40px',
                            'left': '60px',
                            'display': 'block',
                            'float':'center'
                            }
                        ),
        
        ])])])])])

if __name__ == '__main__':
    app.run_server(debug=False)
