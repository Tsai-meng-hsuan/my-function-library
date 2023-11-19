# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:16:34 2023

@author: user
"""

import numpy as np
from tqdm import tqdm
import threading
from time import sleep


key=input("猜猜我是誰? ")
if key=="蔡孟軒":
    file_name=input("input file name: ")
    global start
    start=0
    
    def read_file():
        global start
        waitting_list=[' - ',' \ ',' | ',' / ']
        A=0
        while start==0:
            print('\r','File loading...'+ waitting_list[A] ,end='')
            A=A+1
            if A==4:
                A=0
            sleep(0.25)
        return
    
    t = threading.Thread(target = read_file)
    t.start()
    
    
    
    all_vlot = np.loadtxt(file_name, delimiter=',')
    start=1
    t.join()  # 等待thread_1結束，如果不打join程式會直接往下執行
    
    
    all_avg=[]
    variable_list=[]
    for j in range(len(all_vlot[0,:])):
        variable_list.append(chr(65+j))
                   
    all_avg.append(variable_list)
                            
    avg_number = int(input('幾次取平均:'))
    cal_number=int(len(all_vlot[:,0])/avg_number)
    for i in tqdm(range(cal_number),desc='Calculating...'):
        one_avg=[]
        twoD_array=all_vlot[i*100:(i+1)*100 , :]
        for k in range(len(all_vlot[0,:])):
            oneD_array=twoD_array[:,k]
            avg_oneD_array=np.mean(oneD_array, axis=None)
            one_avg.append(avg_oneD_array)
            
        all_avg.append(one_avg)
    
    path = 'output.txt'
    f = open(path, 'w')
    for l in tqdm(range(len(all_avg)),desc='Output...'):
        for m in range(len(all_vlot[0,:])):
            f.write(str(all_avg[l][m]))
            f.write(' ,')
        f.write("\n")
    f.close()
    print('\n')
    print('Finish !!')

else:
    print("猜錯咯～")
    sleep(3)