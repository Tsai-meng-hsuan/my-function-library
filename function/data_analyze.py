# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:17:29 2023

@author: user
"""

from scipy.optimize import curve_fit
from scipy import signal #滤波等
import pandas as pd
import additional_features
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt



def resample_for_col(rew_data,sample_number):
    data_size=rew_data.shape
    cal_time=int(data_size[0]/sample_number)
    all_avg = pd.DataFrame()
    for i in tqdm(range(int(cal_time)),desc='Resample Processing'): 
        avg_Series = rew_data[i*sample_number:(i+1)*sample_number].mean()
        avg_DF = avg_Series.to_frame()
        T_avg = avg_DF.transpose()
        all_avg = all_avg.append(T_avg, ignore_index=True)
    return(all_avg)


def moving_avg(rew_data_list, avg_sample):
    avg_list=[]
    data_size = len(rew_data_list)
    for i in range(data_size):
        avg = sum(rew_data_list[i : i+avg_sample]/avg_sample)
        avg_list.append(avg)
    return(avg_list)
    

def get_data_shape(rew_data, row0_or_col1):
    answer=rew_data.shape[row0_or_col1]
    return(answer)


def data_mean(rew_data):
    out_put = rew_data.mean()
    return(out_put)

#2個dataframe對位相加
def add_each(new_col_head_list, dataframe_one, dataframe_two):
    size_one = dataframe_one.shape
    size_two = dataframe_two.shape
    new_array = []
    for i in range(size_one[1]):
        one_list = []
        for j in range(size_one[0]):
            answer = dataframe_one.iloc[j,i] + dataframe_two.iloc[j,i]
            one_list.append(answer)
        new_array.append(one_list)
    Trans_array = np.array(new_array).T
    output = pd.DataFrame(Trans_array, columns=new_col_head_list)
    return(output)

#2個dataframe對位相減
def subtraction_each(new_col_head_list, dataframe_one, dataframe_two):
    size_one = dataframe_one.shape
    size_two = dataframe_two.shape
    new_array = []
    for i in range(size_one[1]):
        one_list = []
        for j in range(size_one[0]):
            print(dataframe_one.iloc[j,i])
            answer = dataframe_one.iloc[j,i] - dataframe_two.iloc[j,i]
            one_list.append(answer)
        new_array.append(one_list)
    Trans_array = np.array(new_array).T
    output = pd.DataFrame(Trans_array, columns=new_col_head_list)
    return(output)

#減某一定值
def subtraction_globle(rew_data_DF, one_row_subtraction_dataframe):
    size = rew_data_DF.shape
    add_raw = size[0]
    new_dataframe = pd.DataFrame()
    for i in range(add_raw):
        new_dataframe = new_dataframe.append(one_row_subtraction_dataframe, ignore_index=True)
    out_put = rew_data_DF - new_dataframe
    return(out_put)

#乘某一定值
def multiply_globle(rew_data_DF, multiply_list):
    col_head_list = rew_data_DF.columns.values                                  #取得col 的head
    new_dataframe = pd.DataFrame()
    size = rew_data_DF.shape
    col_number = size[1]
    for i in range(col_number):
        add_dataframe = rew_data_DF.iloc[ : , [i]] * multiply_list[i]           #取得第i欄，分別乘校正係數
        new_dataframe = pd.concat([new_dataframe,add_dataframe],axis=1) 
    return(new_dataframe)


def differential(data_X_list, data_list):
    data_number = len(data_list) 
    diff_x = np.delete(data_X_list, 0)                                          #微分後少一格
    delta_x = np.diff(data_X_list)                                              #每一個取樣點x間距
    delta_data = np.diff(data_list)                                             #每個data前後差值
    diff_data = np.divide(delta_data, delta_x)                                  #data差值/取樣間距 = 斜率
    # plt.plot(diff_x, diff_data, 'r-')
    # plt.show()
    return([diff_x, diff_data])


def integral(data_X_list, data_list, initial_value):
    delta_area = 0
    data_number = len(data_list) 
    # diff_x = np.delete(data_X_list, 0)                                          #微分後少一格
    delta_x = np.diff(data_X_list)                                              #每一個取樣點x間距
    delta_intergral_list=[]
    intergral_list = []
    intergral_list.append(initial_value)
    intergral_value = initial_value
    for i in range(data_number - 1):
        if data_list[i] * data_list[i+1] < 0:
            x_change = abs(data_list[i])/(abs(data_list[i])+abs(data_list[i+1]))*delta_x[i]
            x_before = data_list[i] * x_change /2
            x_after = data_list[i+1] * (delta_x[i] - x_change) / 2
            delta_area = x_before + x_after
            
        if data_list[i] * data_list[i+1] > 0:
            delta_area = (abs(data_list[i]) + abs(data_list[i+1])) * delta_x[i] / 2
            if data_list[i] < 0 :
                delta_area = -delta_area
            
            if data_list[i] > 0 :
                delta_area = delta_area
            
        delta_intergral_list.append(delta_area)
        intergral_value = intergral_value + delta_area
        intergral_list.append(intergral_value)
        
    # plt.plot(data_X_list, intergral_list, 'r-')
    # plt.show()
    return([data_X_list, intergral_list])
    

def peak_value(data_X_list, data_list):
    maxi_index = signal.find_peaks(data_list, distance=1)[0]                   #找極大值的index
    maxi_x_value = data_X_list[maxi_index]
    maxi_data_value = data_list[maxi_index]
    
    mini_index = signal.argrelextrema(data_list ,np.less)[0]                   #极大值点，改为np.less即可得到极小值点
    mixi_x_value = data_list[mini_index]
    mixi_data_value = data_list[mini_index]
    return([mixi_x_value, mixi_data_value, maxi_x_value, maxi_data_value])
    
