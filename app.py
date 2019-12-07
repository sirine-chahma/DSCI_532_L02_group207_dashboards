import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import altair as alt
import pandas as pd
from src import charts as ch
from src import wrangle as wr
from src import themes as th

from vega_datasets import data

app = dash.Dash(__name__, assets_folder='assets', external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.config['suppress_callback_exceptions'] = True
app.title = 'Dash app with pure Altair HTML'

_jumbotron = dbc.Jumbotron(
    [
        html.H1("Barley App", className="display-3"),
        html.Hr(className="my-2"),
        html.P(
            "Barley is part of the major cereal grains used worldwide. Understanding how the annual yield of barley is impacted by the variety or site on which it grows is very important. This dashboard has been created to allow you to explore a dataset containing the annual yield for selected varieties of barley and particular sites, for the years 1931, 1932, or both. It should help you better understand what variety or what site is the most suitable to your situation. If you are wondering:", className="lead"), 
        html.P(
            '- Given some sites and some varieties, what variety of barley had the highest yield during a specific year?', className="lead"),
        html.P(
            '- Given some sites and some varieties, what site had the highest yield during a specific year?', className="lead"),
        html.P(
            '- Given some sites and some varieties, what is the variety of barley with the highest yield for each of the sites?', className="lead"),
        html.P(
            "then this app is exactly what you need! Now, you have no excuse to increase your productivity and have the highest yield as possible! ", className="lead"
        ),
        html.P(
            "Trick: Place your mouse above the different bars to display more information!", className="lead"
        )
    ]
)

data_details = html.Div(
    [
        dbc.Button(
            "Dataset Details",
            id="collapse-button",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody([
                    "We chose the barley dataset from the vega-datasets python package. This dataset shows the yields of 10 different varieties of barley at 6 different sites in Minnesota during the years 1931 and 1932. It first appeared in the 1934 paper 'Statistical Determination of Barley Varietal Adaption' by the three agronomists who led this experiment: F.R. Immer, H.K. Hayes, and L. Powers."
                    ,html.Br(), html.Br(), "The 10 varieties studied are: Velvet, Trebi, No. 457, No. 462, Peatland, No. 475, Manchuria, Glabron, Svansota, and Wisconsin No 38."
                    ,html.Br(), html.Br(), "The 6 sites studied are: University Farm, Waseca, Morris, Crookston, Grand Rapids, and Duluth."

                ])),
    
            id="collapse",
        ),
    ],
    style={"color": 'black'},
)

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

_sidebar_left = dbc.Container(
    [
        html.Br(),
        
        html.H2("Barley Yield", className="display-10"),
        html.P(
            "Choose the filters to see the visualization change", className="lead"
        ),
        html.H6("Year:"),
        dcc.RadioItems(
            id='year_selector',
            options=[
                {'label': '1931', 'value': '1931'},
                {'label': '1932', 'value': '1932'},
                {'label': 'Both', 'value': 'both'}
            ],
            value='both',
            className="display-10"
        ),
        html.Hr(),
        html.H5("Site:"),
        dcc.Dropdown(
            id='site_selector',
            options=[
                {'label': site, 'value': site} for site in wr.barley_df['site'].unique()
            ],
            value=wr.barley_df['site'].unique(),
            className="display-10",
            multi=True,
            style={
                "color": 'black'
            },
        ),
        html.Hr(),
        html.H6("Variety:"),
        dcc.Dropdown(
            id='variety_selector',
            options=[
                {'label': variety, 'value': variety} for variety in wr.barley_df['variety'].unique()
            ],
            value=wr.barley_df['variety'].unique(),
            multi=True,
            style={
                "color": 'black'
            },
        ),
        html.Hr(),
        data_details,        
    ],
    #style=SIDEBAR_STYLE_LEFT,
    style=th.SIDEBAR_STYLE_LEFT,
)


_body = dbc.Container(
    [   dbc.Row(
            [
                dbc.Col(
                    [
                        _jumbotron,    
                    ]
                )
            ]
        ),
        
        dbc.Row(
            [
                dbc.Col([],md=2),
                dbc.Col(
                    [   
                        html.Center(html.H2("Map of the locations of the selected sites")),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='map',
                            height='400',
                            width='1000',
                            style={'border-width': '0'},
                        )
                    ],
                    md=6,
                ),
                dbc.Col(
                    [

                    ],
                    md=1,
                ),
                dbc.Col(
                    [html.Br(),
                    html.Br(),
                     html.P(
                        [
                            "All the sites under study are located in the same state:  ",
                            html.Span(
                                "Minnesota",
                                style={"color": "red"},
                            ),
                            ". To help you visualize more easily where all the sites are, this is a map representing the state of Minnesota and highlighting the location of the different sites with a red dot. "
                            ,"Place your mouse above one of the points to see which site it represents.",
                        ],
                        className="lead"
                    ),
                    ]
                    ,md=3),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Center(
                            [
                                html.H2("Yield per Variety"),
                                
                            ],
                            id="tooltip-ypv"
                        ),
                        dbc.Tooltip(
                            "The following graph allows you to observe the total yield for the selected year(s), for each variety.",
                            target="tooltip-ypv",
                        ),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot1',
                            height='500',
                            width='500',
                            style={'border-width': '0'},
                        ),                  
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.Center(
                            [
                                html.H2("Yield per Site"),
                                
                            ],
                            id="tooltip-yps"
                        ),
                        dbc.Tooltip(
                            "The following graph allows you to observe the total yield for the selected year(s), for each site.",
                            target="tooltip-yps",
                        ),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot2',
                            height='500',
                            width='500',
                            style={'border-width': '0'},
                        ),                  
                    ],
                    md=6
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Center(
                            [
                                html.H2("Yields for the selected varieties for the selected sites"),
                                
                            ],
                            id="tooltip-ysvs"
                        ),
                        dbc.Tooltip(
                            "The following graph allows you to observe the total yield per variety for the selected year(s), for each site. The maximum yield is represented in red.",
                            target="tooltip-ysvs",
                        ),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot3',
                            height='600',
                            width='1200',
                            style={'border-width': '0'},
                        ),              
                        
                    ],
                    md=12
                ),
            ]

        )
    ],
    className="mt-4",
    style=th.BODY,
)

@app.callback(
    Output('map', 'srcDoc'),
    [Input('site_selector', 'value')])
def update_map(site):
    return ch.make_map(site)

@app.callback(
    Output('plot1', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
#create the plot of the yield per variety
def update_yield_per_var(year, site, variety):
    return ch.make_yield_per_var(year, site, variety)

@app.callback(
    Output('plot2', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
#create the plot of the yield per site
def update_yield_per_site(year, site, variety):
    return ch.make_yield_per_site(year, site, variety)

@app.callback(
    Output('plot3', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
#create the faceted chart of the yield per variety for every site
def update_yield_per_site_per_variety(year, site, variety):
    return ch.make_yield_per_site_per_variety(year, site, variety)
   

_layout = html.Div([_sidebar_left,_body])

app.layout = _layout

if __name__ == "__main__":
    app.run_server(debug=True)
