import pandas as pd
import numpy as np
from vega_datasets import data

barley_df = data.barley()


def sanitize(year=None, site=None, variety=None):
    if year == 'both':
        year_temp = [1931, 1932]
    else:
        year_temp = [year]

    # create a list with the selected site(s)
    if not isinstance(site, list) and site != None:
        site_temp = list(site)
    else:
        site_temp = site

    # create a list with the selected varieties
    if not isinstance(variety, list):
        variety_temp = list(variety)
    else:
        variety_temp = variety

    # filter the year
    if(year != None):
        df_temp = barley_df[barley_df['year'].isin(year_temp)]
    # filter the site
    if(site != None):
        df_temp = df_temp[df_temp['site'].isin(site_temp)]
    # filter the variety
    if (variety != None):
        df_temp = df_temp[df_temp['variety'].isin(variety_temp)]

    return df_temp
