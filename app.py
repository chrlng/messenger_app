import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from layouts.page_one_layout import get_page_one_layout
from layouts.page_two_layout import get_page_two_layout


app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP], suppress_callback_exceptions = True)
server = app.server 

app.title = "Messenger Analyzer"
app.layout = html.Div(
    # represents the URL bar, doesn't render anything
    dcc.Location(id = 'url', refresh = False),
    id = "page-content"
)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')], 
)
def display_page(pathname):
    if pathname == '/':
        return get_page_one_layout()
    else: 
        return get_page_two_layout()


if __name__ == '__main__':
    app.run_server(debug = True)