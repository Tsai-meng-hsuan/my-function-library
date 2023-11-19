# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:52:34 2023

@author: user
"""

import matplotlib.pyplot as plt
import pandas as pd

def drew_XY_line(title, X_value, Y_value, line_type):
    plt.title(title)
    plt.plot(X_value ,Y_value , line_type)
    plt.show()
    # plt.plot(a["X_Value"] ,a["SG_Y8"] , 'r-')
    return
    