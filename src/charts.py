import altair as alt
from vega_datasets import data
import pandas as pd
from src import wrangle as wr

def make_map(site):

    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site

    states = alt.topo_feature(data.us_10m.url, feature='states')
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='blue'
    ).properties(
        width=500,
        height=300
    ).transform_filter((alt.datum.id == 27))

    sites = pd.DataFrame({'site': wr.barley_df['site'].unique().tolist(),
                      'lat': [10, 0, -38, -43, 10, 18],
                      'long': [-40, -70, -30, 50, 30, 10]})

    sites_filter = sites[sites['site'].isin(site_temp)]

    points = alt.Chart(sites_filter).mark_circle(
        size=100,
        color='red'
    ).encode(
        x = alt.X('lat:Q', scale=alt.Scale(domain=[-100, 100]), axis=None),
        y = alt.Y('long:Q', scale=alt.Scale(domain=[-100, 100]), axis=None),
        tooltip = ['site']
    )

    chart = (background + points)

    return chart.to_html()

def make_yield_per_var(year, site, variety):

    df_temp = wr.sanitize(year, site, variety)
    
    #create the bar graph
    chart = alt.Chart(df_temp).mark_bar().encode(
        alt.X("variety:N", 
            title="Variety",
            axis = alt.Axis(labelAngle=45)),
        alt.Y("yield:Q",
            title = "Yield (kg/hectare)"),
        alt.Color("year:N", legend=alt.Legend(title="Year")),
        tooltip=['site', 'year', 'yield', 'variety']
        ).properties(width = 320, height=300
        ).configure_title(fontSize=18
        ).configure_axis(
            labelFontSize=14, 
            titleFontSize=18)

    return chart.to_html()

def make_yield_per_site(year, site, variety):

    df_temp = wr.sanitize(year, site, variety)
    
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
    ).properties(width = 320, height=300
    ).configure_title(fontSize=18
    ).configure_axis(
        labelFontSize=14, 
        titleFontSize=18)
    
    return chart.to_html()

def make_yield_per_site_per_variety(year, site, variety):

    df_temp = wr.sanitize(year=year, variety=variety)
    
    #create a list with the selected site(s)
    if not isinstance(site, list):
        site_temp = list(site)
    else:
        site_temp = site
        
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
            alt.Y("variety:N", 
                title= sites,
                axis = alt.Axis(labelAngle=0)),
            alt.X("yield:Q",
                title = "Yield (kg/hectare)"),
            #set the color of the maximum as orange
            color=alt.condition(
                alt.datum.variety == my_max, 
                alt.value('red'),     
                alt.value('grey')),
            tooltip=['site', 'yield', 'variety']
            ).properties(width = 220, height=230)

            #add this chart to the list that contains all the charts
            my_graphs.append(chart)
    
    #change the way all the charts will be displayed regarding to the number of charts
    if len(my_graphs) == 1:
        my_chart = my_graphs[0]
        my_chart = my_chart.configure_title(fontSize=18
        ).configure_axis(   
        labelFontSize=14, 
        titleFontSize=18
        ).configure_title(fontSize=25)
    elif len(my_graphs) == 2:
        my_chart = alt.hconcat(my_graphs[0], my_graphs[1]).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=14, 
        titleFontSize=18
        )
    elif len(my_graphs) == 3:
        my_chart = alt.hconcat(my_graphs[0], my_graphs[1], my_graphs[2]).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=14, 
        titleFontSize=18
        )
    elif len(my_graphs) == 4:
        my_chart = alt.vconcat(alt.hconcat(my_graphs[0], my_graphs[1]), 
                              alt.hconcat(my_graphs[2], my_graphs[3])
        ).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=14, 
        titleFontSize=18
        )
    elif len(my_graphs) == 5:
        my_chart = alt.vconcat(alt.hconcat(my_graphs[0], my_graphs[1], my_graphs[2]), 
                              alt.hconcat(my_graphs[3], my_graphs[4])
        ).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=14, 
        titleFontSize=18
        )
    elif len(my_graphs) == 6:
        my_chart = alt.vconcat(alt.hconcat(my_graphs[0], my_graphs[1], my_graphs[2]), 
                              alt.hconcat(my_graphs[3], my_graphs[4], my_graphs[5])
        ).configure_title(fontSize=18
        ).configure_axis(
        labelFontSize=14, 
        titleFontSize=18
        )
    else : 
        my_chart = alt.Chart(df_temp).mark_bar()

    return my_chart.to_html()