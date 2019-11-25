import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import altair as alt
import vega_datasets as vega_datasets
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, assets_folder='assets', external_stylesheets=[dbc.themes.BOOTSTRAP])
df = vega_datasets.data.barley()
body = dbc.Container(
    [
        dbc.Row(
            [
                html.Div([
                    
                    dbc.Button(
                        "Collapse Menu", color='primary', id='left', className="mr-1"
                    ),

                    dbc.Col(
                        dbc.Collapse(
                            dbc.Card(
                        [
                            html.H1("Barley Yield History"),
                            html.H2("Filters:"),
                            html.Label("Year"),
                            dcc.RadioItems(
                                id='year_selector',
                                options=[
                                    {'label': 1931, 'value': 1931},
                                    {'label': 1932, 'value': 1932},
                                    {'label': 'All', 'value': 'both'}
                                ],
                                value=1931,
                                labelStyle={'display': 'inline-block', 'text-align': 'justify',
                                'marginRight': 10,
                                'marginBottom': 5}
                            ),
                            html.Label('Site'),
                            dcc.Dropdown(
                                id='site_selector',
                                options=[
                                    {'label': site, 'value': site} for site in df['site'].unique()
                                ],
                                value=['University Farm', 'Grand Rapids'],
                                multi=True,
                                style={'height': '150px', 'width': '300px', 'marginBottom': 5}
                            ),
                            html.Label('Variety', style={'marginTop': 5}),
                            dcc.Dropdown(
                                id='variety_selector',
                                options=[
                                    {'label': variety, 'value': variety} for variety in df['variety'].unique()
                                ],
                                value=['Manchuria', 'Velvet'],
                                multi=True,
                                style={'height': '150px', 'width': '300px', 'marginTop': 5}
                            )
                        ]), id = "left-collapse"),
                align='start')
                ], style={'min-height': '400px', 'border': '2px lightblue solid', 'overflowY': 'scroll'}),
                dbc.Col(
                    [
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='yield_per_var',
                            height='450',
                            width='450',
                            style={'border-width': '0px', 'overflowX': 'scroll'}
                        )
                    ]),
                dbc.Col(
                    [
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='yield_per_site',
                            height='450',
                            width='450',
                            style={'border-width': '0px', 'overflowX': 'scroll'}
                        )
                    ]
                )
            ]
        )
    ]
)

server = app.server

app.title = 'Trial App of Sketch'
app.layout = html.Div([body])

@app.callback(
    Output('yield_per_var', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
def make_yield_per_var(year, site, variety):

    if year == 'both':
        year_temp = [1931, 1932]
    else:
        year_temp = [year]
    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site
    if not isinstance(variety, list):
        variety_temp = list(variety)
    else:
        variety_temp = variety

    df_temp = df[df['year'].isin(year_temp)]
    df_temp = df_temp[df_temp['site'].isin(site_temp)]
    df_temp = df_temp[df_temp['variety'].isin(variety_temp)]

    chart = alt.Chart(df_temp).mark_bar().encode(
        alt.X("variety:N", 
            title="Variety",
            sort=alt.EncodingSortField(field="yield", op="sum", order='ascending'),
            axis = alt.Axis(labelAngle=45)),
        alt.Y("yield:Q",
            title = "Yield (kg/hectare)"),
        alt.Color("year:N", legend=alt.Legend(title="Year"))
        ).properties(title="Yield per variety", width = 300
        ).configure_title(fontSize=18
        ).configure_axis(
            labelFontSize=10, 
            titleFontSize=13).interactive()

    return chart.to_html()

@app.callback(
    Output('yield_per_site', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
def make_yield_per_site(year, site, variety):

    if year == 'both':
        year_temp = [1931, 1932]
    else:
        year_temp = [year]
    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site
    if not isinstance(variety, list):
        variety_temp = list(variety)
    else:
        variety_temp = variety

    df_temp = df[df['year'].isin(year_temp)]
    df_temp = df_temp[df_temp['site'].isin(site_temp)]
    df_temp = df_temp[df_temp['variety'].isin(variety_temp)]

    
    chart = alt.Chart(df_temp, width=600).mark_bar().encode(
        alt.X("site:N", 
            title="Site",
            sort=alt.EncodingSortField(field="yield", op="sum", order='ascending'),
            axis = alt.Axis(labelAngle=45)),
        alt.Y("yield:Q",
            title = "Yield (kg/hectare)"),
        alt.Color("year:N", legend=alt.Legend(title="Year"))
    ).properties(title="Yield per site", width = 300
    ).configure_title(fontSize=18
    ).configure_axis(
        labelFontSize=11, 
        titleFontSize=13)

    return chart.to_html()

@app.callback(
    Output("left-collapse", "is_open"),
    [Input("left", "n_clicks")],
    [State("left-collapse", "is_open")],
)
def toggle_left(n_left, is_open):
    if n_left:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)