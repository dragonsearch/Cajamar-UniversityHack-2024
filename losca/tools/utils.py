import pandas as pd
import numpy as np
import os



def mean_values_biorreactor(bt, th, datetime_init, datetime_end, id_biorreactor, lot):

    #Get the data between the range of datetimes and matching the from id_biorreactor, transposing the dataframe
    bt_dttm_range = bt[(bt['f_h_bt'].astype(str).str[:-6] >= datetime_init) 
                       & (bt['f_h_bt'].astype(str).str[:-6] <= datetime_end) 
                       & (bt['id_bio'] == id_biorreactor)].drop(columns=['f_h_bt', 'id_bio'])

    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    bt_mean_dttm_range = pd.DataFrame(bt_dttm_range.mean(), index = bt_dttm_range.columns).transpose()

    #Adding lot column
    bt_mean_dttm_range['lote'] = lot

    #Adding columns for temparture and humidity
    bt_mean_dttm_range = pd.concat([bt_mean_dttm_range, t_h_biocent(th, datetime_init, datetime_end, 'biorreactor')], axis=1)


    return bt_mean_dttm_range

    
def mean_values_centrifuga(ct, th, datetime_init, datetime_end, id_centrifuga, lot):

    #Get the data between the range of datetimes and matching the from id_biorreactor, transposing the dataframe
    ct_dttm_range = ct[(ct['f_h_ct'].astype(str).str[:-6] >= datetime_init) 
                       & (ct['f_h_ct'].astype(str).str[:-6] <= datetime_end) 
                       & (ct['id_centr'] == id_centrifuga)].drop(columns=['f_h_ct', 'id_centr'])

    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    ct_mean_dttm_range = pd.DataFrame(ct_dttm_range.mean(), index = ct_dttm_range.columns).transpose()

    #Adding lot column
    ct_mean_dttm_range['lote'] = lot

    #Adding columns for temparture and humidity
    ct_mean_dttm_range = pd.concat([ct_mean_dttm_range, t_h_biocent(th, datetime_init, datetime_end, 'centrifuga')], axis=1)

    return ct_mean_dttm_range


def mean_t_h_principal(th, datetime_init, datetime_end):

    #Get the data between the range of datetimes
    main_dock_th = th[((th['datetime_th'].astype(str).str[:-6] >= datetime_init)) 
                        & (th['datetime_th'].astype(str).str[:-6] <= datetime_end)].loc[:,'t_al_princ_th':'h_al_princ_th']
    
    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    main_dock_th_mean = pd.DataFrame(main_dock_th.mean(), index = main_dock_th.columns).transpose()
                                           
    return main_dock_th_mean

def mean_t_h_produccion(th, datetime_init, datetime_end):

    #Get the data between the range of datetimes
    main_dock_th = th[((th['datetime_th'].astype(str).str[:-6] >= datetime_init)) 
                        & (th['datetime_th'].astype(str).str[:-6] <= datetime_end)].loc[:,'t_al_prod_th':'h_al_prod_th']
    
    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    main_dock_th_mean = pd.DataFrame(main_dock_th.mean(), index = main_dock_th.columns).transpose()
                                           
    return main_dock_th_mean



def t_h_biocent(df, datetime_init, datetime_end, type):
    if type == 'biorreactor':
        df_dttm_range = df[(df['datetime_th'].astype(str).str[:-6] >= datetime_init) 
                           & (df['datetime_th'].astype(str).str[:-6] <= datetime_end)].loc[:,'t_bio_th':'h_bio_th'].mean().to_frame().transpose() 
    elif type == 'centrifuga':
        df_dttm_range = df[(df['datetime_th'].astype(str).str[:-6] >= datetime_init) 
                           & (df['datetime_th'].astype(str).str[:-6] <= datetime_end)].loc[:,'t_cent_th':'h_cent_th'].mean().to_frame().transpose()
    else:
        raise ValueError('type must be "biorreactor" or "centrifuga"')
    
    return df_dttm_range
    
