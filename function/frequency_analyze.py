# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 16:01:48 2023

@author: user
"""

from scipy.fft import fft, fftfreq
import numpy as np

try1=avgdata.to_numpy()

print(try1[:,0])
N = 8000     # Number of sample points(會改變精度，但不改變主頻位置，頻譜點數為N/2)
sample_rate=200   #頻譜頻寬為取樣平率之半
T = 1.0 / sample_rate     # sample spacing(取樣時間差，會影響頻率範圍，1s/sample_rate=週期)

# x = np.linspace(0.0, N*T, N, endpoint=False)     #np.linspace(初值, 終值, 點數, endpoint=False)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

x=try1[:,0]
y=try1[:,2]
yf = fft(y)
xf = fftfreq(N, T)[:N//2]     #(除以2取整數)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.show()

plt.plot(x, y)
# def data_FFT(rew_data, Number of sample points, sample_rate):
    
    
#     return