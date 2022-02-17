
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pathlib
from app import app
from dash import dash_table
import dash_bootstrap_components as dbc

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


df = pd.read_csv(DATA_PATH.joinpath("statsfordash.csv"))

layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
])

@app.callback(
    Output('tbl_out', 'children'), Input('tbl', 'active_cell')
)

def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"
