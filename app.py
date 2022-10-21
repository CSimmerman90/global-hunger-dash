import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('global-hunger-index.csv')
available_countries = df['entity'].unique()

df2 = pd.read_csv('share-of-children-underweight.csv')
underweight_country = df2['country'].unique()

fig = px.line(df, x="year", y="global_hunger_index", color='entity', markers=True)
fig2 = px.bar(df2, x="year", y="underweight_percent", color='country')

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Global Hunger Index'),
        html.Div(children='''
            Analysis of the Global Hunger Index.
        '''),
        html.Label('Select Countries'),
        dcc.Dropdown(id= 'demo-dropdown', options=[{"value": i, "label": i} for i in available_countries],
                     value= ['Afghanistan'], multi=True),
        dcc.Graph(
            id='display-selected-values',
            figure=fig
        ),
    ]),
    html.Div([
        html.H1(children='Hello Dash V2'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),
        html.Label('Multi-Select Dropdown 2'),
        dcc.Dropdown(id= 'demo2-dropdown', options=[{"value": i, "label": i} for i in underweight_country],
                     value= ['Afghanistan'], multi=True),
        dcc.Graph(
            id='display-selected-values-2',
            figure=fig2
        ), 
    ]),
])

@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    ts = df[df["entity"].isin(value)]
    fig = px.line(ts, x="year", y="global_hunger_index", color="entity", markers=True)
    return fig

@app.callback(
    dash.dependencies.Output('display-selected-values-2', 'figure2'),
    [dash.dependencies.Input('demo2-dropdown', 'value')])
def update_output2(value):
    ts2 = df2[df2["country"].isin(value)]
    fig2 = px.bar(df2, x="year", y="underweight_percent", color='country')
    return fig2

if __name__ == '__main__':
    app.run_server(debug=True)