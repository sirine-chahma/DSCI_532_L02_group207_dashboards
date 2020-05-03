import pandas as pd
import numpy as np
from vega_datasets import data

barley_df = data.barley()


def sanitize(year=None, site=None, variety=None):

    """
    A helper function that filters the data frame depending on what is selected in the toolbar.

    Arguments:
    year -- A list of integers that provides the years for which the dataset will be filtered for.
     Default = None.
    site -- A list of strings that provides the sites for which the dataset will be filtered for. 
     Default = None.
    variety -- A list of strings that provides the sites for which the dataset will be filtered for.
     Default = None.

    Returns:
    dataframe 
     A Pandas dataframe object that contains the filtered dataset, to be used for graphing purposes.

    Examples:
    sanitize(["1931"], ["Grand Rapids"], ["Manchuria"])

    """


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
