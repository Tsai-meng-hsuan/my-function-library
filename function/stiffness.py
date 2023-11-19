# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 21:47:55 2023

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

data= data_arrange.load_txt_data('202303_CYC030動態PY(MV).txt', '\t', 0)

drew_figure.drew_XY_line("SG_Y8" ,data["2Y"] ,data["2P"] , 'g-')

a=data.iloc[1,1]

n = 0
Y_max = []
P_max = []
Y_min = [0]
P_min = [0]

Y_col = 15
P_col = 16
while True:
    Y_max_index = n*20+46
    P_max_index = n*20+46
    Y_min_index = n*20+56
    P_min_index = n*20+56
    
    Y_max.append(data.iloc[Y_max_index,Y_col])
    P_max.append(data.iloc[P_max_index,P_col])
    Y_min.append(data.iloc[Y_min_index,Y_col])
    P_min.append(data.iloc[P_min_index,P_col])
    
    n = n+1
    if n*20+56 >= 4216:
        break

k_list = []
n_list = []
for i in range(200):
    k = (P_max[i]-P_min[i])/(Y_max[i]-Y_min[i])
    k_list.append(k)
    n_list.append(i+1)
    
drew_figure.drew_XY_line("SG_Y8" ,n_list ,k_list , 'g-')
