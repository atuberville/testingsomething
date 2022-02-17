import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


df = pd.read_csv(DATA_PATH.joinpath("statsfordash.csv"))
df['visit_date'] = pd.to_datetime(df.visit_date)
df.sort_values(by=['visit_date'])


layout = html.Div([
    html.Div([

        html.Br(),
        html.Label(['Select Your Competitors'],style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Dropdown(id='team_one',
            options=[{'label':x, 'value':x} for x in df.sort_values('Your Team')['Your Team'].unique()],
            value='Air Force',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose The Team...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),

        dcc.Dropdown(id='team_two',
            options=[{'label':x, 'value':x} for x in df.sort_values('Your Team')['Your Team'].unique()],
            value='Akron',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose The Team...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),

        dcc.Dropdown(id='team_three',
            options=[{'label':x, 'value':x} for x in df.sort_values('Your Team')['Your Team'].unique()],
            value='Alabama',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose The Team...',
            className='form-dropdown',
            style={'width':"90%"},
            persistence='string',
            persistence_type='memory'),
    ],className='three columns'),

    html.Div([
        dcc.Graph(id='penaltygraph')
    ],className='two columns'),
    
    html.Div(className='row', children=[
        html.Div(className='parent', children=[
            dcc.Graph(id='offrushgraph', className='plot'),
            html.Div(className='spacer'),
            dcc.Graph(id='defrushgraph', className='plot'),
        ])
    ]),
    
    html.Div([
        dcc.Graph(id='offpassgraph')
    ],className='two columns'),
    
    html.Div([
        dcc.Graph(id='defpassgraph')
    ],className='two columns'),



])

@app.callback(
    Output('penaltygraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph(first_team, second_team, third_team):
    dff=df[(df['Your Team']==first_team)|
           (df['Your Team']==second_team)|
           (df['Your Team']==third_team)]
    # print(dff[:5])

    fig = px.bar(dff, x="visit_date", y="a_penalty_yards", color='Your Team',color_discrete_sequence=px.colors.qualitative.G10, height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Penalty Yards'},
                      title={'text':'Penalty Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig


@app.callback(
    Output('offrushgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph2(first_team, second_team, third_team):
    dff=df[(df['Your Team']==first_team)|
           (df['Your Team']==second_team)|
           (df['Your Team']==third_team)]
    # print(dff[:5])

    fig = px.bar(dff, x="visit_date", y="a_offense_rush_yards", color='Your Team',color_discrete_sequence=px.colors.qualitative.G10, height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Rush Yards'},
                      title={'text':'Offense Rush Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig
@app.callback(
    Output('defrushgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph3(first_team, second_team, third_team):
    dff=df[(df['Your Team']==first_team)|
           (df['Your Team']==second_team)|
           (df['Your Team']==third_team)]
    # print(dff[:5])

    fig = px.bar(dff, x="visit_date", y="a_defense_rush_yards", color='Your Team', color_discrete_sequence=px.colors.qualitative.G10,height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Rush Yards'},
                      title={'text':'Defense Rush Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig

@app.callback(
    Output('defpassgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph4(first_team, second_team, third_team):
    dff=df[(df['Your Team']==first_team)|
           (df['Your Team']==second_team)|
           (df['Your Team']==third_team)]
    # print(dff[:5])

    fig = px.bar(dff, x="visit_date", y="a_defense_pass_yards", color='Your Team',color_discrete_sequence=px.colors.qualitative.G10, height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Pass Yards'},
                      title={'text':'Defense Pass Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig

@app.callback(
    Output('offpassgraph','figure'),
    [Input('team_one','value'),
     Input('team_two','value'),
     Input('team_three','value')]
)

def build_graph5(first_team, second_team, third_team):
    dff=df[(df['Your Team']==first_team)|
           (df['Your Team']==second_team)|
           (df['Your Team']==third_team)]
    # print(dff[:5])

    fig = px.bar(dff, x="visit_date", y="a_offense_pass_yards", color='Your Team',color_discrete_sequence=px.colors.qualitative.G10, height=600)
    fig.update_layout(xaxis={'title':'Game Date'},
                      yaxis={'title': 'Pass Yards'},
                      title={'text':'Offense Pass Yards at the Half',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig