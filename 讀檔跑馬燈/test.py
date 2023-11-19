# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:41:20 2023

@author: user
"""


from time import sleep

waitting_list=[' - ',' \ ',' | ',' / ']
A=0
while 1:
    print('\r','file loading...'+ waitting_list[A] ,end='')
    A=A+1
    if A==4:
        A=0
    sleep(0.25)
    