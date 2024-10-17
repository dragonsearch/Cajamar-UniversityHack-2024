import pandas as pd
import numpy as np
import os

def mean_values_biorreactor(bt, th, datetime_init, datetime_end, id_biorreactor):
    """ 
    Gets the mean, min, max, init and end values of the biorreactor between the range of datetimes and matching the id_biorreactor
    """
    bt_dttm_range = bt[(bt['f_h_bt'] >= datetime_init) 
                       & (bt['f_h_bt'] <= datetime_end) 
                    & (bt['id_bio'] == id_biorreactor)]

    # Sort the dataframe by f_h_bt
    bt_dttm_range = bt_dttm_range.sort_values(by='f_h_bt').reset_index(drop=True).drop(columns=['f_h_bt', 'id_bio'])

    # Create new dataframe with the same columns as the original dataframe and same types
    bt_mean_dttm_range = pd.DataFrame(bt_dttm_range.mean(), index = bt_dttm_range.columns).transpose()

    # Get the first and last
    # Create new dataframe with the first values of the original dataframe
    bt_first_dttm_range = bt_dttm_range.head(1).reset_index(drop=True).copy()
    bt_last_dttm_range = bt_dttm_range.tail(1).reset_index(drop=True).copy()

    for column in bt_first_dttm_range.columns:
        bt_first_dttm_range.rename(columns={column: column + '_first'}, inplace=True)
    # Create new dataframe with the last values of the original dataframe

    for column in bt_last_dttm_range.columns:
        bt_last_dttm_range.rename(columns={column: column + '_last'}, inplace=True)

    # Create new dataframe with the max values of the original dataframe, rename the columns adding _max
    bt_max_dttm_range = pd.DataFrame(bt_dttm_range.max(), index = bt_dttm_range.columns).transpose()
    for column in bt_max_dttm_range.columns:
        bt_max_dttm_range.rename(columns={column: column + '_max'}, inplace=True)

    # Create new dataframe with the min values of the original dataframe
    bt_min_dttm_range = pd.DataFrame(bt_dttm_range.min(), index = bt_dttm_range.columns).transpose()
    for column in bt_min_dttm_range.columns:
        bt_min_dttm_range.rename(columns={column: column + '_min'}, inplace=True)

    # Join them all 
    bt_mean_dttm_range = pd.concat([bt_mean_dttm_range, bt_max_dttm_range, bt_min_dttm_range, bt_first_dttm_range, bt_last_dttm_range], axis=1)

    #Adding columns for temparture and humidity
    bt_mean_dttm_range = pd.concat([bt_mean_dttm_range, t_h_biocent(th, datetime_init, datetime_end, 'biorreactor')], axis=1)


    return bt_mean_dttm_range


    
def mean_values_centrifuga(ct, th, datetime_init, datetime_end, id_centrifuga):
    """ 
    Gets the mean, min, max, init and end values of the biorreactor between the range of datetimes and matching the id_centrifuga
    """
    #Get the data between the range of datetimes and matching the from id_biorreactor, transposing the dataframe
    ct_dttm_range = ct[(ct['f_h_ct'] >= datetime_init) 
                    & (ct['f_h_ct'] <= datetime_end) 
                & (ct['id_centr'] == id_centrifuga)]
    
    # Sort the dataframe by f_h_ct
    ct_dttm_range = ct_dttm_range.sort_values(by='f_h_ct').reset_index(drop=True).drop(columns=['f_h_ct', 'id_centr'])

    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    ct_mean_dttm_range = pd.DataFrame(ct_dttm_range.mean(), index = ct_dttm_range.columns).transpose()
    # Create new dataframe with the first values of the original dataframe
    ct_first_dttm_range = ct_dttm_range.head(1).reset_index(drop=True).copy()
    ct_last_dttm_range = ct_dttm_range.tail(1).reset_index(drop=True).copy()
    for column in ct_first_dttm_range.columns:
        ct_first_dttm_range.rename(columns={column: column + '_first'}, inplace=True)
    # Create new dataframe with the last values of the original dataframe
    for column in ct_last_dttm_range.columns:
        ct_last_dttm_range.rename(columns={column: column + '_last'}, inplace=True)
    # Create new dataframe with the max values of the original dataframe, rename the columns adding _max
    ct_max_dttm_range = pd.DataFrame(ct_dttm_range.max(), index = ct_dttm_range.columns).transpose()
    for column in ct_max_dttm_range.columns:
        ct_max_dttm_range.rename(columns={column: column + '_max'}, inplace=True)
    # Create new dataframe with the min values of the original dataframe
    ct_min_dttm_range = pd.DataFrame(ct_dttm_range.min(), index = ct_dttm_range.columns).transpose()
    for column in ct_min_dttm_range.columns:
        ct_min_dttm_range.rename(columns={column: column + '_min'}, inplace=True)
    # Join them all
    ct_mean_dttm_range = pd.concat([ct_mean_dttm_range, ct_max_dttm_range, ct_min_dttm_range, ct_first_dttm_range, ct_last_dttm_range], axis=1)

    #Adding columns for temparture and humidity
    ct_mean_dttm_range = pd.concat([ct_mean_dttm_range, t_h_biocent(th, datetime_init, datetime_end, 'centrifuga')], axis=1)

    return ct_mean_dttm_range


def mean_t_h_principal(th, datetime_init, datetime_end):
    """
    Get the mean values of the temperature and humidity of the almacen principal between the range of datetimes
    """
    #Get the data between the range of datetimes
    main_dock_th = th[((th['datetime_th'] >= datetime_init)) 
                        & (th['datetime_th'] <= datetime_end)].loc[:,'t_al_princ_th':'h_al_princ_th']
    
    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    main_dock_th_mean = pd.DataFrame(main_dock_th.mean(), index = main_dock_th.columns).transpose()
                                           
    return main_dock_th_mean

def mean_t_h_produccion(th, datetime_init, datetime_end):
    """
    Get the mean values of the temperature and humidity of the almacen de produccion between the range of datetimes
    """
    #Get the data between the range of datetimes
    main_dock_th = th[((th['datetime_th'] >= datetime_init)) 
                        & (th['datetime_th'] <= datetime_end)].loc[:,'t_al_prod_th':'h_al_prod_th']
    
    #Mean values and storage in a dataframe with the same columns, name columns as the original dataframe
    main_dock_th_mean = pd.DataFrame(main_dock_th.mean(), index = main_dock_th.columns).transpose()
                                           
    return main_dock_th_mean



def t_h_biocent(df, datetime_init, datetime_end, type):
    """
    Get the mean values of the temperature and humidity of the biorreactor or centrifuga between the range of datetimes
    """
    if type == 'biorreactor':
        df_dttm_range = df[(df['datetime_th'] >= datetime_init) 
                           & (df['datetime_th'] <= datetime_end)].loc[:,'t_bio_th':'h_bio_th'].mean().to_frame().transpose()
    elif type == 'centrifuga':
        df_dttm_range = df[(df['datetime_th'] >= datetime_init) 
                           & (df['datetime_th'] <= datetime_end)].loc[:,'t_cent_th':'h_cent_th'].mean().to_frame().transpose()
    else:
        raise ValueError('type must be "biorreactor" or "centrifuga"')
    
    return df_dttm_range