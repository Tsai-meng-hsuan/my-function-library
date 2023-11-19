# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:28:19 2023

@author: user
"""



# import numpy
# import pandas as pd

import pandas as pd
import numpy as np



def load_txt_data(file_name, separator, skip_row):                              #載入data
    rew_data = pd.read_table(file_name, sep=separator , skiprows=range(skip_row)) #sep:分隔符號 ； skip:開始行
    print(rew_data)
    return(rew_data)


def out_put_csv(rew_data, file_name):
    rew_data.to_csv(file_name, index=True)
    print('finish file out put !!')
    return()


def time_select(rew_data, time_col_name, start_time, end_time):
    if end_time == 'end':
        end_row=rew_data.tail(1)                                                # 看后 n 行
        end_time=end_row.iloc[0][time_col_name]  
    out_put_min=rew_data[rew_data[time_col_name] >= start_time ]
    out_put_band=out_put_min[out_put_min[time_col_name] <= end_time ]
    return(out_put_band)


def col_select(rew_data,Colume_name_list):                                      # col設定
    out_put=rew_data[Colume_name_list]                                          # out_put=rew_data[["name", "chinese"]]
    return(out_put)


def col_recombine(*DataFrame):
    new_dataframe = pd.DataFrame()                                              #新增DataFrame
    in_put_DF_number = len(DataFrame)
    for i in range(int(in_put_DF_number)):
        new_dataframe=pd.concat([new_dataframe,DataFrame[i]],axis=1)            #組合多個DataFrame
    print('Finish col recombine !')
    return(new_dataframe)


def add_one_setting_col(rew_data_DF, new_col_head_Str, new_col_location_index, col_value):
    size = rew_data_DF.shape
    new_array = np.linspace(col_value, col_value, size[0])                      #創建定值單欄矩陣
    # new_col = pd.DataFrame(new_array, columns=[new_col_head_Str])             #array轉DF，並設定head
    rew_data_DF.insert(new_col_location_index, new_col_head_Str, new_array)
    out_put = rew_data_DF
    return(out_put)

def read_head_N(file_name, N):                                                  #讀取前幾行，一行一行讀，用for迴圈重複
    line_list = []
    file = open(file_name, "r")
    for i in range(N):
        one_line = file.readline()
        line_list.append(one_line)
    return line_list