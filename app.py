import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('global-hunger-index.csv')
available_countries = df['entity'].unique()

fig = px.line(df, x="year", y="global_hunger_index", color='entity', markers=True)


app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Global Hunger Index', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown(id= 'demo-dropdown', options=[{"value": i, "label": i} for i in available_countries],
                     value= ['Afghanistan'], multi=True),
        dcc.Graph(id='display-selected-values', figure=fig)
    ])

@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    ts = df[df["entity"].isin(value)]
    fig = px.line(ts, x="year", y="global_hunger_index", color="entity", markers=True)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)