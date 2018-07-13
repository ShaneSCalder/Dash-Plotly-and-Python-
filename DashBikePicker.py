import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


app = dash.Dash()
df = pd.read_csv('wheels.csv')

app.Layout = html.Div([
        dcc.RadioItems(
            id='wheels',
            options=[{'label':i, 'value':i} for i in df['wheels'].unique()],
            value=1
        ),
        html.Div('wheels-output'),
        html.Hr(),
        dcc.RadioItems(
            id ='colors',
            options=[{'label':i, 'value':i} for i in df['color'].unique()],
            value='blue'
        ),
        html.Div(id='colors-output')
],style={'fontFamily':'helvetica','fontSize':18})


#@app.callback(Output('wheels-output','children'),
#[Input('wheels','value')])
#def callback_a(wheels_value):
    #return 'You chose "{}"'.format(wheels_value)


#[Input('colors','value')])
#def callback_b(colors_value):
    #return 'You chose "{}"'.format(colors_value)

app.config['suppress_callback_exceptions']=True     
@app.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')])
def callback_a(wheels_value):
    return 'You\'ve selected "{}"'.format(wheels_value)
app.config['suppress_callback_exceptions']=True
@app.callback(
    Output('colors-output', 'children'),
    [Input('colors', 'value')])
def callback_b(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)

if __name__ == '__main__':
    app.run_server()
