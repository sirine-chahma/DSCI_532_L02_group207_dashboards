import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
import dash
import charts as ch
import wrangle as wr
import altair as alt
from dash.dependencies import Input, Output



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True

# custom navbar based on https://getbootstrap.com/docs/4.1/examples/dashboard/
_dashboard = dbc.Navbar(
    sticky="top",
    children=[
        dbc.Col(dbc.NavbarBrand("BaRley", href="#"), sm=3, md=2),
        #dbc.Col(dbc.Input(type="search", placeholder="Search here")),
        dbc.Col(),
        dbc.Col(
            dbc.Nav(dbc.NavItem(dbc.NavLink("Sign out")), navbar=True),
            width="auto",
        ),
    ],
    color="dark",
    dark=True,
)


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE_LEFT = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    #"background-color": "#f8f9fa",
    "background-color": '#343A40', 
    "color": 'white',
}

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE_RIGHT = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    #"background-color": "#f8f9fa",
    "background-color": '#343A40', 
    "color": 'white',
}

BODY_STYLE = {
   "background-color": '#cccdcf', 
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

_sidebar_left = dbc.Container(
    [
        html.Br(),
        html.Br(),
        
        html.H2("Barley Yield", className="display-4"),
        html.Hr(),
        html.P(
            "Choose the filters to see the visualization change", className="lead"
        ),
        html.Hr(),
        html.H5("Year:"),
        dcc.RadioItems(
            id='year_selector',
            options=[
                {'label': '1931', 'value': '1931'},
                {'label': '1932', 'value': '1932'},
                {'label': 'All', 'value': 'both'}
            ],
            value='both',
            className="display-6"
        ),
        html.Hr(),
        html.Br(),
        html.H5("Site:"),
        dcc.Dropdown(
            id='site_selector',
            options=[
                {'label': site, 'value': site} for site in wr.barley_df['site'].unique()
            ],
            value=wr.barley_df['site'].unique(),
            multi=True,
            style={
                "color": 'black'
            },
        ),
        html.Hr(),
        html.Br(),
        html.H5("Variety:"),
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
        html.Hr()
    ],
    style=SIDEBAR_STYLE_LEFT,
)

_sidebar_right = dbc.Container( #html.Div(
    [
        html.Br(),
        html.Br(),
        
        html.Center(html.H2("Legend", className="display-8")),
        html.Hr(),
        html.Hr()
    ],
    style=SIDEBAR_STYLE_RIGHT,
    fluid = True,
)

_body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Center(html.H2("Yield per Variety")),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot1',
                            height='500',
                            width='500',
                            style={'border-width': '0'},
                            ################ The magic happens here
                            #srcDoc=open('./Lecture1_charts/horsepower_vs_displacement.html').read()
                            #srcDoc=ch.make_plot().to_html()
                            #srcDoc= ch.make_plot().to_html()
                            ################ The magic happens here
                        ),                  
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.Center(html.H2("Yield per Site")),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot2',
                            height='500',
                            width='500',
                            style={'border-width': '0'},
                            ################ The magic happens here
                            #srcDoc=open('./Lecture1_charts/horsepower_vs_displacement.html').read()
                            srcDoc=ch.make_plot().to_html()
                            ################ The magic happens here
                        ),                  
                    ],
                    md=6
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Center(html.H2("Yields for the selected varieties for the selected sites")),
                        html.Iframe(
                            sandbox='allow-scripts',
                            id='plot3',
                            height='1000',
                            width='1000',
                            style={'border-width': '0'},
                            ################ The magic happens here
                            #srcDoc=open('./Lecture1_charts/horsepower_vs_displacement.html').read()
                            srcDoc=ch.make_plot().to_html()
                            ################ The magic happens here
                        ),              
                        
                    ],
                    md=12
                ),
            ]

        )
    ],
    className="mt-4",
)

#_layout = html.Div([_dashboard, _sidebar_left, _body, _sidebar_right])

_layout = html.Div([_sidebar_left, _body, _sidebar_right])

class DemoLayoutPage:
    def for_path(self, component):
        return _layout


# @app.callback(
#     dash.dependencies.Output('plot1', 'srcDoc'),
#     [dash.dependencies.Input('year_selector', 'value'),
#     dash.dependencies.Input('variety_selector', 'value'),
#     dash.dependencies.Input('site_selector', 'value')])
# def update_plot(years, varieties, sites):
#     print(years)
#     print(varieties)
#     print(sites)
#     plot = ch.make_plot()
#     return plot


@app.callback(
    Output('plot1', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
#create the plot of the yield per variety
def make_yield_per_var(year, site, variety):

    if year == 'both':
        year_temp = [1931, 1932]
    else:
        year_temp = [year]

    #create a list with the selected site(s)
    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site
    
    #create a list with the selected varieties
    if not isinstance(variety, list):
        variety_temp = list(variety)
    else:
        variety_temp = variety

    #filter the year
    df_temp = wr.barley_df[wr.barley_df['year'].isin(year_temp)]
    #filter the site
    df_temp = df_temp[df_temp['site'].isin(site_temp)]
    #filter the variety
    df_temp = df_temp[df_temp['variety'].isin(variety_temp)]

    #create the bar graph
    chart = alt.Chart(df_temp).mark_bar().encode(
        alt.X("variety:N", 
            title="Variety",
            sort=alt.EncodingSortField(field="yield", op="sum", order='ascending'),
            axis = alt.Axis(labelAngle=45)),
        alt.Y("yield:Q",
            title = "Yield (kg/hectare)"),
        alt.Color("year:N", legend=alt.Legend(title="Year")),
        tooltip=['site', 'year', 'yield', 'variety']
        ).properties(width = 350, height=300
        ).configure_title(fontSize=18
        ).configure_axis(
            labelFontSize=10, 
            titleFontSize=13).interactive()

    return chart.to_html()

@app.callback(
    Output('plot2', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
#create the plot of the yield per site
def make_yield_per_site(year, site, variety):

    #create a list with the selected year(s)
    if year == 'both':
        year_temp = [1931, 1932]
    else:
        year_temp = [year]

    #create a list with the selected site(s)
    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site
    
    #create a list with the selected varieties
    if not isinstance(variety, list):
        variety_temp = list(variety)
    else:
        variety_temp = variety

    #filter the year
    df_temp = wr.barley_df[wr.barley_df['year'].isin(year_temp)]

    #filter the site
    df_temp = df_temp[df_temp['site'].isin(site_temp)]

    #filter the variety
    df_temp = df_temp[df_temp['variety'].isin(variety_temp)]

    #create the bar graph
    chart = alt.Chart(df_temp).mark_bar().encode(
        alt.X("site:N", 
            title="Site",
            sort=alt.EncodingSortField(field="yield", op="sum", order='ascending'),
            axis = alt.Axis(labelAngle=45)),
        alt.Y("yield:Q",
            title = "Yield (kg/hectare)"),
        alt.Color("year:N", legend=alt.Legend(title="Year")),
        tooltip=['site', 'year', 'yield', 'variety']
    ).properties(width = 350, height=300
    ).configure_title(fontSize=18
    ).configure_axis(
        labelFontSize=11, 
        titleFontSize=13).interactive()
    
    return chart.to_html()

@app.callback(
    Output('plot3', 'srcDoc'),
    [Input('year_selector', 'value'), Input('site_selector', 'value'), Input('variety_selector', 'value')])
#create the faceted chart of the yield per variety for every site
def make_yield_per_site_per_variety(year, site, variety):

    #create a list with the selected year(s)
    if year == 'both':
        year_temp = [1931, 1932]
    else:
        year_temp = [year]

    #create a list with the selected site(s)
    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site

    #create a list with the selected varieties
    if not isinstance(variety, list):
        variety_temp = list(variety)
    else:
        variety_temp = variety
    
    #filter the year
    df_temp = wr.barley_df[wr.barley_df['year'].isin(year_temp)]

    #filter the variety
    df_temp = df_temp[df_temp['variety'].isin(variety_temp)]

    #my_graphs is a list that will contain all the different bar graphs that will be faceted
    my_graphs = []

    if df_temp.empty == False : 
        for sites in site_temp:
            #filter the site
            df_temp_site = df_temp[df_temp['site'] == sites]
            #create a data frame to find the maximum value of the yield
            df_max = (df_temp_site.drop(columns=['year'])
                            .groupby(['variety', 'site'])
                            .agg('sum')
                            .sort_values('yield', ascending=False)
                            .reset_index()
                    )
            #my_max is the variety that had the highest yield

            my_max = df_max['variety'][0]

            #create the bar graph
            chart = alt.Chart(df_max).mark_bar().encode(
            alt.X("variety:N", 
                title= sites,
                sort=alt.EncodingSortField(field="yield", op="sum", order='ascending'),
                axis = alt.Axis(labelAngle=45)),
            alt.Y("yield:Q",
                title = "Yield (kg/hectare)"),
            #set the color of the maximum as orange
            color=alt.condition(
                alt.datum.variety == my_max, 
                alt.value('red'),     
                alt.value('grey')),
            tooltip=['site', 'yield', 'variety']
            ).properties(width = 250, height=200).interactive()

            #add this chart to the list that contains all the charts
            my_graphs.append(chart)
    
    #change the way all the charts will be displayed regarding to the number of charts
    if len(my_graphs) == 1:
        my_chart = my_graphs[0]
        my_chart = my_chart.configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=10, 
        titleFontSize=12
        ).configure_title(fontSize=25)
    elif len(my_graphs) == 2:
        my_chart = alt.hconcat(my_graphs[0], my_graphs[1]).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=10, 
        titleFontSize=12
        )
    elif len(my_graphs) == 3:
        my_chart = alt.hconcat(my_graphs[0], my_graphs[1], my_graphs[2]).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=10, 
        titleFontSize=12
        )
    elif len(my_graphs) == 4:
        my_chart = alt.vconcat(alt.hconcat(my_graphs[0], my_graphs[1]), 
                              alt.hconcat(my_graphs[2], my_graphs[3])
        ).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=10, 
        titleFontSize=12
        )
    elif len(my_graphs) == 5:
        my_chart = alt.vconcat(alt.hconcat(my_graphs[0], my_graphs[1], my_graphs[2]), 
                              alt.hconcat(my_graphs[3], my_graphs[4])
        ).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=10, 
        titleFontSize=12
        )
    elif len(my_graphs) == 6:
        my_chart = alt.vconcat(alt.hconcat(my_graphs[0], my_graphs[1], my_graphs[2]), 
                              alt.hconcat(my_graphs[3], my_graphs[4], my_graphs[5])
        ).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=10, 
        titleFontSize=12
        )
    else : 
        my_chart = alt.Chart(df_temp).mark_bar()

    return my_chart.to_html()

if __name__ == "__main__":
    app.layout = _layout
    app.run_server(debug=True)





