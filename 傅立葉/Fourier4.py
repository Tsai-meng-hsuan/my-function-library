# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:07:13 2021

@author: memgal
"""

from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import math
import numpy as np
import xlwings as xw
import os
import tkinter as tk
from tkinter.filedialog import (askopenfilename, askopenfilenames, askdirectory, asksaveasfilename)
from tqdm import tqdm

#def integrate(V0,S0,sample_num,time_gap,acceleration_duration):
#    v_list=[V0]
#    s_list=[S0]
#    for i in range(sample_num):
#        v_list.append(v_list[i]+time_gap*acceleration_duration[i])
#    for j in range(len(v_list)):
#        s_list.append(s_list[j]+time_gap*v_list[j])
#    print(s_list)
    
#本程式可輸入<單一加速度歷時檔案.txt>，進行基線修正、傅立葉分析、濾波、反傅立葉分析及積分

root = tk.Tk()
initial_file=askopenfilenames() #選取檔案並紀錄絕對位置
root.mainloop()

first_line=2 #數據開始的第一行

initial_data_name=[] #讀取原始檔案的檔名
for i in range(len(initial_file)):
    initial_data_name.append(initial_file[i].split('/')) #檔案絕對位置分割
    
final_data=[]
for j in range(len(initial_file)): 
    f = open(initial_file[j]) #開啟原始檔並讀取資料
    initial_data = f.readlines()
    f.close()
    
    acceleration=[]
    for i in range(len(initial_data)-first_line): #寫入加速度資料
        split_data=initial_data[i+first_line].split()
        acceleration.append(float(split_data[1]))
    
    before1000_acceleration=[]
    for i in range(1000): #前1000筆資料基線修正
        before1000_acceleration.append(acceleration[i])
        
    mean=sum(before1000_acceleration)/len(before1000_acceleration) #前1000筆資料之平均值
    
    baseline_correction_acceleration=[]
    for i in range(len(initial_data)-2): #基線修正(原始加速度-前1000筆資料平均值)
        baseline_correction_acceleration.append(acceleration[i]-mean)
        
    baseline_correction_acceleration_array=np.array(baseline_correction_acceleration)
    final_data.append(baseline_correction_acceleration_array)

log_point_number=math.log(len(baseline_correction_acceleration),2) #計算總打點數的log2值
sample_num=2**(int(log_point_number)+1) #快速傅立葉總點數
sampling_rate=200 #打點頻率(Hz,t=0.005)


fd = np.linspace(0.0, sampling_rate, sample_num, endpoint=False)

for i in range(sample_num): #過於點數補零
    try:
        exsit=baseline_correction_acceleration[i]
    except:
        baseline_correction_acceleration.append(0)
        
vib_fft = fft(baseline_correction_acceleration)
mag = 2/sample_num * np.abs(vib_fft) # Magnitude

plt.figure(1)
plt.plot(fd[0:int(sample_num/2)], mag[0:int(sample_num/2)])
plt.xlabel('Hz')
plt.ylabel('Mag')

fft_fre=fd[0:int(sample_num/2)]
fft_acceleration=mag[0:int(sample_num/2)]

#反傅立葉分析
filter_fft_acceleration=[]
for i in tqdm(range(int(len(vib_fft)))):
    if fd[i]>=0.1 and fd[i]<=30:
        filter_fft_acceleration.append(vib_fft[i])
    elif fd[i]>=170 and fd[i]<=199.9:
        filter_fft_acceleration.append(vib_fft[i])
    else:
        filter_fft_acceleration.append(complex(0,0)) #0.1~30Hz濾波
        
ifft_filter_acceleration=ifft(filter_fft_acceleration)#反傅立葉(轉成時域加速度)

ifft_time=[]
for i in range(sample_num):
    ifft_time.append(0.005*i)
array_ifft_time=np.array(ifft_time)

plt.figure(2)
plt.plot(array_ifft_time, ifft_filter_acceleration)
plt.xlabel('Time')
plt.ylabel('A-Mag(cm/s^2)')

v_list=[complex(0,0)]
s_list=[complex(0,0)]
for i in range(sample_num-1):
    v_list.append(v_list[i]+0.005*ifft_filter_acceleration[i])
for j in range(len(v_list)-1):
    s_list.append(s_list[j]+0.005*v_list[j])

array_v_list=np.array(v_list)        
plt.figure(3)
plt.plot(array_ifft_time, v_list)
plt.xlabel('Time')
plt.ylabel('V-Mag(cm/s)')

array_s_list=np.array(s_list) 
plt.figure(4)
plt.plot(array_ifft_time, s_list)
plt.xlabel('Time')
plt.ylabel('S-Mag(cm)')

new_file=open('New_acceleration_'+initial_data_name[0][-3]+'_'+initial_data_name[0][-2], mode='w')
new_file.write('acceleration'+' \n')
for k in range(len(ifft_time)):
    new_file.write(str(ifft_filter_acceleration[k].real)+' \n')
new_file.close()
        





    
    