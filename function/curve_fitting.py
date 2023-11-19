# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:04:38 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



def polynomial_25(x, a, b, c, d, e, f):
    return a + b*(x**1) +c*(x**2.5) + d*(x**3) + e*(x**4) + f*(x**5)


def exp_sin(x, a, b, c, d, e):
    return np.exp(a*x+b)*np.sin(c*x+d)+e


def curve_fitting(xdata, ydata, start_X, end_X, fitting_type):
    xdata = np.array(xdata)
    ydata = np.array(ydata)
    # plt.plot(xdata, ydata, 'bo', label='data')
    popt, pcov = curve_fit(fitting_type, xdata, ydata, maxfev=50000)
    fitting_x = np.linspace(start_X, end_X, 200)
    fitting_data = fitting_type(np.linspace(start_X, end_X, 200), *popt)
    # plt.plot(fitting_x, fitting_data, 'r-')
    # plt.show()
    
    print(popt)
    return([popt, fitting_x, fitting_data])




    
