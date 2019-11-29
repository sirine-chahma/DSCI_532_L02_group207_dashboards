import altair as alt
import wrangle as wr
import themes as th

# register the custom theme under a chosen name
alt.themes.register('mds_special', th.mds_special)

# enable the newly registered theme
#alt.themes.enable('mds_special')

def make_plot(data=wr.barley_df, x_axis='variety', y_axis = 'yield', x_type = 'nominal', y_type='quantitative', title="Variety vs Yield"):
    #alt.themes.enable('mds_special')
    chart = alt.Chart(data).mark_bar().encode(
                alt.X(x_axis, type=x_type,title = x_axis),
                alt.Y(y_axis, type=y_type,title = y_axis),
                alt.Color('year:N', legend=None),
                tooltip = [x_axis, y_axis]
            ).properties(title=title, width=400, height=300).interactive()

    return chart
