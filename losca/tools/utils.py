import pandas as pd
import numpy as np
import os



def mean_values_biorreactor(df, datetime_init, datetime_end, id_biorreactor, lot):

    #Get the data between the range of datetimes and matching the from id_biorreactor, transposing the dataframe
    bt_dttm_range = df[(pd.to_datetime(df['f_h_bt'].astype(str).str[:-6]) >= pd.to_datetime(datetime_init)) 
                       & (pd.to_datetime(df['f_h_bt'].astype(str).str[:-6]) <= datetime_end) 
                       & (df['id_bio'] == id_biorreactor)].drop(columns=['f_h_bt', 'id_bio'])

    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    bt_mean_dttm_range = pd.DataFrame(bt_dttm_range.mean(), index = bt_dttm_range.columns).transpose()

    #Adding lot column
    bt_mean_dttm_range['lote'] = lot


    return bt_mean_dttm_range

    
def mean_values_centrifuga(df, datetime_init, datetime_end, id_centrifuga, lot):

    #Get the data between the range of datetimes and matching the from id_biorreactor, transposing the dataframe
    ct_dttm_range = df[(pd.to_datetime(df['f_h_ct'].astype(str).str[:-6]) >= pd.to_datetime(datetime_init)) 
                       & (pd.to_datetime(df['f_h_ct'].astype(str).str[:-6]) <= datetime_end) 
                       & (df['id_centr'] == id_centrifuga)].drop(columns=['f_h_ct', 'id_centr'])

    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    ct_mean_dttm_range = pd.DataFrame(ct_dttm_range.mean(), index = ct_dttm_range.columns).transpose()

    #Adding lot column
    ct_mean_dttm_range['lote'] = lot

    return ct_mean_dttm_range