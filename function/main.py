# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:04:41 2023

@author: user
"""

import data_arrange
import drew_figure
import data_analyze
import curve_fitting
import pandas as pd
import numpy as np
from curve_fitting import exp_sin
from curve_fitting import polynomial_25
import matplotlib.pyplot as plt
import numpy as np

select_list_S7 = ["X_Value", "load_Y","SG_Y5", "SG_Y6", "SG_Y7", "SG_Y8", "SG_Y9", "SG_Y10"]
select_list_S9 = ["X_Value","SG_Y2", "SG_Y3", "SG_Y4", "SG_Y11", "SG_Y12", "SG_Y13", "SG_Y14", "LDT_20", "LDT_29"]
select_moment = ["SG_Y2", "SG_Y3", "SG_Y4", "SG_Y5", "SG_Y6", "SG_Y7", "SG_Y8", "SG_Y9", "SG_Y10", "SG_Y11", "SG_Y12", "SG_Y13", "SG_Y14"]
select_under_mudline_M = ["SG_Y4", "SG_Y5", "SG_Y6", "SG_Y7", "SG_Y8", "SG_Y9", "SG_Y10", "SG_Y11", "SG_Y12", "SG_Y13", "SG_Y14"]
# select_moment = ["X_Value","SG_Y2", "SG_Y3", "SG_Y4", "SG_Y5", "SG_Y6", "SG_Y7", "SG_Y8", "SG_Y9", "SG_Y10", "SG_Y11", "SG_Y12", "SG_Y13", "SG_Y14"]
calibration_coefficient = [1, 2.1331, 1.8541, 2.537 ,0.4396, 0.4421, 0.4402, 0.4486, 0.4914, 0.5082, 0.4724, 5.1379, 5.2265, 4.7599, 2.7969, 2.7997, -26.461]
SG_location_list = [-0.1, -0.05, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.19, 0.22, 0.27]
SG_mudline_location_list = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.19, 0.22, 0.27]
time_index_202212CYC030 = [127+1*40, 127+2*40, 127+10*40, 127+29*40, 127+98*40, 127+40*190]
time_index_202212CYC010 = [85+1*40, 85+2*40, 85+9*40, 85+29*40, 85+100*40, 85+300*40, 85+449*40]
time_index_202303CYC030 = [45+1*20, 41+3*20, 41+10*20, 41+29*20, 41+99*20, 41+190*20]
EI = 26.34640779
delta_hu = 5.2
depth_list = [19, 37, 56, 74, 93, 111, 130, 148]
#=======================================================================================================================

#載入電壓資料
data_S7 = data_arrange.load_txt_data('S7_test_202303CYC030.lvm', '\t', 22)
data_S9 = data_arrange.load_txt_data('S9_test_202303CYC030.lvm', '\t', 22)

#取平均
avgdata_S7 = data_analyze.resample_for_col(data_S7, 100)
avgdata_S9 = data_analyze.resample_for_col(data_S9, 100)

#取出應變計+LDT+loadY
select_S7 = data_arrange.col_select(avgdata_S7, select_list_S7)
select_S9 = data_arrange.col_select(avgdata_S9, select_list_S9)

#資料排序
recombine_data = data_arrange.col_recombine(data_arrange.col_select(select_S9, ["X_Value","SG_Y2", "SG_Y3", "SG_Y4"]),
                                            data_arrange.col_select(select_S7, ["SG_Y5", "SG_Y6", "SG_Y7", "SG_Y8", "SG_Y9", "SG_Y10"]),
                                            data_arrange.col_select(select_S9, ["SG_Y11", "SG_Y12", "SG_Y13", "SG_Y14", "LDT_20", "LDT_29"]),
                                            data_arrange.col_select(select_S7, ["load_Y"]))

#取初值
initial_value = data_arrange.time_select(recombine_data, "X_Value", 0, 1).mean()
initial_value_T = initial_value.to_frame().T
drew_figure.drew_XY_line("SG_Y8" ,recombine_data["X_Value"] ,recombine_data["SG_Y8"] , 'g-')

#減初值
recombine_shift_data = data_analyze.subtraction_globle(recombine_data, initial_value_T)
drew_figure.drew_XY_line("SG_Y8", recombine_data["X_Value"] ,recombine_shift_data["SG_Y8"] , 'r-')

#乘校正係數
real_physical_value = data_analyze.multiply_globle( recombine_shift_data, calibration_coefficient)

#取出彎矩並加入樁底0彎矩
moment = data_arrange.col_select(real_physical_value, select_moment)
under_mudline_moment = data_arrange.col_select(real_physical_value, select_under_mudline_M)

add_moment = data_arrange.add_one_setting_col(moment, 'bot', 13, 0)
add_mudline_moment = data_arrange.add_one_setting_col(under_mudline_moment, 'bot', 11, 0)

#單一特定時間彎矩分布
one_moment_distribution = add_moment.iloc[127]
drew_figure.drew_XY_line("", one_moment_distribution ,SG_location_list , 'r*-')
one_mudline_moment_distribution = add_mudline_moment.iloc[127]
drew_figure.drew_XY_line('', one_mudline_moment_distribution ,SG_mudline_location_list , 'r*-')

#單一特定時間彎矩回歸線
curve_fitting_coeffecient = curve_fitting.curve_fitting(SG_mudline_location_list, one_mudline_moment_distribution, 0, 0.27, exp_sin)

#多組特定時間彎矩回歸線
fitting_output_list=[]
for i in time_index_202303CYC030:
    print(i)
    one_mudline_moment_distribution = add_mudline_moment.iloc[i]
    drew_figure.drew_XY_line('', one_mudline_moment_distribution ,SG_mudline_location_list , 'r*-')
    a = curve_fitting.curve_fitting(SG_mudline_location_list, one_mudline_moment_distribution, 0, 0.27, exp_sin)
    fitting_output_list.append(a)
    
#為分計算
V = data_analyze.differential(fitting_output_list[1][1], fitting_output_list[1][2])
P = data_analyze.differential(V[0], V[1])

#積分計算
S = data_analyze.integral(fitting_output_list[3][1], fitting_output_list[3][2]/EI, -0.02)
Y = data_analyze.integral(S[0], S[1], 0.0031)

#取出邊界LDT及Moment
LDT_value = data_arrange.col_select(real_physical_value, ['X_Value', 'LDT_20', 'LDT_29'])
M0 = data_arrange.col_select(real_physical_value, ['X_Value', 'SG_Y2', 'SG_Y4'])
size = real_physical_value.shape
add_raw = size[0]

LDT20_value = LDT_value.iloc[:,1]
LDT29_value = LDT_value.iloc[:,2]
MomentY2 = data_arrange.col_select(real_physical_value, ['SG_Y2'])
MomentY4 = data_arrange.col_select(real_physical_value, ['SG_Y4'])

#計算斜率邊界條件LDT + M/EI
dif_LDT = (LDT20_value - LDT29_value)
dif_LDT_DF = dif_LDT.to_frame()
S0 = data_analyze.multiply_globle(dif_LDT_DF, [-1/5.2])
delta_S0 = data_analyze.add_each(['test'], MomentY2, MomentY4)
delta_S1 = data_analyze.multiply_globle(delta_S0, [0.1/2/EI])
delta_S1_seri = delta_S1.squeeze()
S0_seri = S0.squeeze()
ini_S = (S0_seri + delta_S1_seri)

#計算位移邊界條件
delta_Dis = data_analyze.multiply_globle(S0, [15.5])
ini_Dis = (LDT29_value.squeeze() + delta_Dis.squeeze())/100


all_list = []
for i in range(add_raw):
    print(i)
    one_M = add_mudline_moment.iloc[i]
    fitting_output = curve_fitting.curve_fitting(SG_mudline_location_list, one_M, 0, 0.27, exp_sin)
    # fitting_output_list.append(fitting_coef)
    V = data_analyze.differential(fitting_output[1], fitting_output[2])
    P = data_analyze.differential(V[0], V[1])
    S = data_analyze.integral(fitting_output[1], fitting_output[2]/EI, ini_S[i])
    Y = data_analyze.integral(S[0], S[1], ini_Dis[i])
    all_list.append([fitting_output[2], V[1], P[1], fitting_output[2]/EI, S[1]])

time_Z_P = []
time_Z_Y = []


for i in range(add_raw):
    time_Z_P.append(all_list[i][2][depth_list[7]]) 
    time_Z_Y.append(all_list[i][4][depth_list[7]]) 

    
drew_figure.drew_XY_line("LDT_20", recombine_shift_data["X_Value"] ,real_physical_value["LDT_20"] , 'r-')
drew_figure.drew_XY_line("LDT_29", recombine_shift_data["X_Value"] ,real_physical_value["LDT_29"] , 'r-')
drew_figure.drew_XY_line("dif_LDT", recombine_shift_data["X_Value"] ,dif_LDT , 'r-')
drew_figure.drew_XY_line('S0', recombine_shift_data["X_Value"] ,S0 , 'r-')
drew_figure.drew_XY_line("delta_S0", recombine_shift_data["X_Value"] ,delta_S1 , 'r-')
drew_figure.drew_XY_line('ini_S', recombine_shift_data["X_Value"] ,ini_S , 'r-')
drew_figure.drew_XY_line("LDT29", recombine_shift_data["X_Value"] ,LDT29_value , 'r-')
drew_figure.drew_XY_line("delta_Dis", recombine_shift_data["X_Value"] ,delta_Dis , 'r-')
drew_figure.drew_XY_line("ini_Dis", recombine_shift_data["X_Value"] ,ini_Dis , 'r-')
drew_figure.drew_XY_line("PY", time_Z_Y ,time_Z_P , 'r-')
# print(LDT_value.iloc[0,2])
# new_col_head_list, dataframe_one, dataframe_two = ['test'], MomentY2, MomentY4
# new_dataframe = pd.DataFrame() 
# size_one = dataframe_one.shape
# size_two = dataframe_two.shape
# new_array = []
# for i in range(size_one[1]):
#     one_list = []
#     for j in range(size_one[0]):
#         print(dataframe_one.iloc[j,i])
#         answer = dataframe_one.iloc[j,i] - dataframe_two.iloc[j,i]
#         one_list.append(answer)
#     new_array.append(one_list)
# test1 = np.array(new_array).T
# test2 = pd.DataFrame(test1,
#     columns=['111'])