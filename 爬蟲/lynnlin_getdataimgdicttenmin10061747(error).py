qqqqqqqqqq# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:04:00 2020

@author: memgal
@modify: lynnlin
"""

from time import sleep
from time import strftime
from time import time
from selenium import webdriver
import requests
import hashlib
import os
from selenium.common.exceptions import NoSuchElementException
import xlwings as xw
import csv
import datetime
import traceback


#excel24整理===============================================================================
def excel24(comptime,T):
    ln=0
    location=[]
    datumcomptime = datetime.datetime.strptime(comptime, "%Y/%m/%d %H:%M")
    for i in range(len(allotherlist)):
        datacomptime = datetime.datetime.strptime(allotherlist[i][5], "%Y/%m/%d %H:%M")
        if datacomptime >= datumcomptime:
            location.append(i)
    app = xw.App(visible=True,add_book=False)
    wb = app.books.add()
    #wb = xw.Book('initialdataimg.xlsx')
    sht = wb.sheets[0]           
    for j in range(len(location)):
        sht.range('a'+str(j+1)).value =numberlist[location[ln]]
        sht.range('b'+str(j+1)).value =titlelist[location[ln]]
        sht.range('c'+str(j+1)).value =allotherlist[location[ln]][0]
        sht.range('d'+str(j+1)).value =allotherlist[location[ln]][1]
        sht.range('e'+str(j+1)).value =allotherlist[location[ln]][2]
        sht.range('f'+str(j+1)).value =allotherlist[location[ln]][3]
        sht.range('g'+str(j+1)).value =allotherlist[location[ln]][4]
        sht.range('h'+str(j+1)).value =allotherlist[location[ln]][5]
        sht.range('i'+str(j+1)).value =allotherlist[location[ln]][6]
        sht.range('j'+str(j+1)).value =allotherlist[location[ln]][7]
        sht.range('k'+str(j+1)).value =allotherlist[location[ln]][8]
        sht.range('l'+str(j+1)).value =allotherlist[location[ln]][9]
        ln=ln+1
    
    ln=0
    for k in range(len(location)):
        try:
            sht.range('m'+str(k+1)).value = dict1[sht.range('b'+str(location[ln]+1)).value]
            sht.range('n'+str(k+1)).value = dict2[sht.range('b'+str(location[ln]+1)).value]
            sht.range('o'+str(k+1)).value = dict3[sht.range('b'+str(location[ln]+1)).value]
        except:
            sht.range('o'+str(k+1)).value = 'Ot'
#                        sht.range('m'+str(i+1)).value = 'error'
#                        sht.range('n'+str(i+1)).value = 'error'
            print('name error')
        ln=ln+1
    try :
        sleep(1)
        os.remove('initialdata'+T+'.xlsx')
    except:
        print('initialdata'+T+' error')
    sleep(2)
    #新建initialdata====================================================================================
    wb.save('initialdata'+T+'.xlsx')
    print('save'+' initialdata'+T)
    sleep(1)
    app.quit()
    sleep(1)
    
    
#24小時時間資料整理=========================================================================
def hours(T):
    x =datetime.datetime.now()+datetime.timedelta(hours=-T)
    day1=x.year
    day2=x.month #會拿到 12
    day3=x.day # 會拿到 5
    day4=x.hour   #時
    day5=x.minute #分
    if day2 < 10: #月
        day2='0'+str(day2)
    if day3 < 10: #日
        day3='0'+str(day3)
    if day4 < 10: #時
        day4='0'+str(day4)
    if day5 < 10: #分
        day5='0'+str(day5)
    hours=str(day1)+'/'+str(day2)+'/'+str(day3)+' '+str(day4)+':'+str(day5)
    return hours
#LINE回報錯誤==========================================================================
def lineNotifyMessage(token, msg):
  headers = {
      "Authorization": "Bearer " + token, 
      "Content-Type" : "application/x-www-form-urlencoded"
  }
	
  payload = {'message': msg}
  r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
  return r.status_code
	
  # 修改為你要傳送的訊息內容
message = '系統錯誤 程式中斷'
#  # 修改為你的權杖內容
#token = 'A8awq49cUUIt2LnFsE28ZJpRDmQ0uhM25pEXd80iTgl'


#時間資料=============================================================================
waittime='----'
second=0
second2=1
timelist=['00:02:00','00:12:00','00:22:00','00:32:00','00:42:00','00:52:00',
          '01:02:00','01:12:00','01:22:00','01:32:00','01:42:00','01:52:00',
          '02:02:00','02:12:00','02:22:00','02:32:00','02:42:00','02:52:00',
          '03:02:00','03:12:00','03:22:00','03:32:00','03:42:00','03:52:00',
          '04:02:00','04:12:00','04:22:00','04:32:00','04:42:00','04:52:00',
          '05:02:00','05:12:00','05:22:00','05:32:00','05:42:00','05:52:00',
          '06:02:00','06:12:00','06:22:00','06:32:00','06:42:00','06:52:00',
          '07:02:00','07:12:00','07:22:00','07:32:00','07:42:00','07:52:00',
          '08:02:00','08:12:00','08:22:00','08:32:00','08:42:00','08:52:00',
          '09:02:00','09:12:00','09:22:00','09:32:00','09:42:00','09:52:00',
          '10:02:00','10:12:00','10:22:00','10:32:00','10:42:00','10:52:00',
          '11:02:00','11:12:00','11:22:00','11:32:00','11:42:00','11:52:00',
          '12:02:00','12:12:00','12:22:00','12:32:00','12:42:00','12:52:00',
          '13:02:00','13:12:00','13:22:00','13:32:00','13:42:00','13:52:00',
          '14:02:00','14:12:00','14:22:00','14:32:00','14:42:00','14:52:00',
          '15:02:00','15:12:00','15:22:00','15:32:00','15:42:00','15:52:00',
          '16:02:00','16:12:00','16:22:00','16:32:00','16:42:00','16:52:00',
          '17:02:00','17:12:00','17:22:00','17:32:00','17:42:00','17:52:00',
          '18:02:00','18:12:00','18:22:00','18:32:00','18:42:00','18:52:00',
          '19:02:00','19:12:00','19:22:00','19:32:00','19:42:00','19:52:00',
          '20:02:00','20:12:00','20:22:00','20:32:00','20:42:00','20:52:00',
          '21:02:00','21:12:00','21:22:00','21:32:00','21:42:00','21:52:00',
          '22:02:00','22:12:00','22:22:00','22:32:00','22:42:00','22:52:00',
          '23:02:00','23:12:00','23:22:00','23:32:00','23:42:00','23:52:00','10:13:00',
          #================================================================
          '00:02:01','00:12:01','00:22:01','00:32:01','00:42:01','00:52:01',
          '01:02:01','01:12:01','01:22:01','01:32:01','01:42:01','01:52:01',
          '02:02:01','02:12:01','02:22:01','02:32:01','02:42:01','02:52:01',
          '03:02:01','03:12:01','03:22:01','03:32:01','03:42:01','03:52:01',
          '04:02:01','04:12:01','04:22:01','04:32:01','04:42:01','04:52:01',
          '05:02:01','05:12:01','05:22:01','05:32:01','05:42:01','05:52:01',
          '06:02:01','06:12:01','06:22:01','06:32:01','06:42:01','06:52:01',
          '07:02:01','07:12:01','07:22:01','07:32:01','07:42:01','07:52:01',
          '08:02:01','08:12:01','08:22:01','08:32:01','08:42:01','08:52:01',
          '09:02:01','09:12:01','09:22:01','09:32:01','09:42:01','09:52:01',
          '10:02:01','10:12:01','10:22:01','10:32:01','10:42:01','10:52:01',
          '11:02:01','11:12:01','11:22:01','11:32:01','11:42:01','11:52:01',
          '12:02:01','12:12:01','12:22:01','12:32:01','12:42:01','12:52:01',
          '13:02:01','13:12:01','13:22:01','13:32:01','13:42:01','13:52:01',
          '14:02:01','14:12:01','14:22:01','14:32:01','14:42:01','14:52:01',
          '15:02:01','15:12:01','15:22:01','15:32:01','15:42:01','15:52:01',
          '16:02:01','16:12:01','16:22:01','16:32:01','16:42:01','16:52:01',
          '17:02:01','17:12:01','17:22:01','17:32:01','17:42:01','17:52:01',
          '18:02:01','18:12:01','18:22:01','18:32:01','18:42:01','18:52:01',
          '19:02:01','19:12:01','19:22:01','19:32:01','19:42:01','19:52:01',
          '20:02:01','20:12:01','20:22:01','20:32:01','20:42:01','20:52:01',
          '21:02:01','21:12:01','21:22:01','21:32:01','21:42:01','21:52:01',
          '22:02:01','22:12:01','22:22:01','22:32:01','22:42:01','22:52:01',
          '23:02:01','23:12:01','23:22:01','23:32:01','23:42:01','23:52:01'
          ]
#tenmin資料===========================================================================
checktime=0
beforerainyn=0
tenmin=[]
inttenmin=[]
nowtimelist=[]
tenminlist=['/html/body/div[3]/main/div[1]/div/table/tbody/tr[1]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[2]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[3]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[4]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[5]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[6]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[7]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[8]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[9]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[10]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[11]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[12]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[13]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[14]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[15]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[16]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[17]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[18]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[19]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[20]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[21]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[22]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[23]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[24]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[25]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[26]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[27]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[28]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[29]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[30]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[31]/td[2]/span',
            '/html/body/div[3]/main/div[1]/div/table/tbody/tr[32]/td[2]/span'
            ]

#sgetdataimgdict資料==========================================================================
rain3mm=0
yn=1
allotherlist=[]
otherlist=[]
alldata=[]
initialdata=[]
numberlist=[]
titlelist=[]
dict1={}
dict2={}
dict3={}
xpathlist=['//*[@id="ctable"]/tbody/tr[1]/td[1]',
           '//*[@id="ctable"]/tbody/tr[2]/td[1]',
           '//*[@id="ctable"]/tbody/tr[3]/td[1]',
           '//*[@id="ctable"]/tbody/tr[4]/td[1]',
           '//*[@id="ctable"]/tbody/tr[5]/td[1]',
           '//*[@id="ctable"]/tbody/tr[6]/td[1]',
           '//*[@id="ctable"]/tbody/tr[7]/td[1]',
           '//*[@id="ctable"]/tbody/tr[8]/td[1]',
           '//*[@id="ctable"]/tbody/tr[9]/td[1]',
           '//*[@id="ctable"]/tbody/tr[10]/td[1]'
           ]
titlexpathlist=['//*[@id="ctable"]/tbody/tr[1]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[2]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[3]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[4]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[5]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[6]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[7]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[8]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[9]/td[2]/img',
                '//*[@id="ctable"]/tbody/tr[10]/td[2]/img',
                ]

#otherxpathlist=[['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/span[3]'],
#           ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[3]/span',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[4]/span[1]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[4]/span[2]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[5]/span[1]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[5]/span[2]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[6]/span[1]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[7]/span[1]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[7]/span[2]',
#            '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[7]/span[3]'],
#            ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[3]/span',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[4]/span[1]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[4]/span[2]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[5]/span[1]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[5]/span[2]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[6]/span[1]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[7]/span[1]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[7]/span[2]',
#             '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[7]/span[3]'],
#             ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[7]/span[3]'],
#              ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[7]/span[3]'],
#            ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[7]/span[3]'],
#            ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[7]/span[3]'],
#             ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[7]/span[3]'],
#            ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[7]/span[3]'],
#            ['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[3]/span',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[4]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[4]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[5]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[5]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[6]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[7]/span[1]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[7]/span[2]',
#           '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[7]/span[3]']
#           ]

otherxpathlist=[['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[7]/span[3]'],
           ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[3]/span',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[4]/span[1]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[4]/span[2]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[5]/span[1]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[5]/span[2]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[6]/span[1]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[7]/span[1]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[7]/span[2]',
            '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[7]/span[3]'],
            ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[3]/span',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[4]/span[1]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[4]/span[2]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[5]/span[1]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[5]/span[2]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[6]/span[1]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[7]/span[1]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[7]/span[2]',
             '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[7]/span[3]'],
             ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[7]/span[3]'],
              ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[7]/span[3]'],
            ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[7]/span[3]'],
            ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[7]/span[3]'],
             ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[7]/span[3]'],
            ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[7]/span[3]'],
            ['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[3]/span',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[4]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[4]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[5]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[5]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[6]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[7]/span[1]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[7]/span[2]',
           '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[7]/span[3]']
           ]
            
#imglist=['/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[8]/a/img',
#         '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[8]/a/img'
#         ]

imglist=['/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[3]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[4]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[5]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[7]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[8]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[9]/td[8]/a/img',
         '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[10]/td[8]/a/img'
         ]
while True:
    try:
        #抓取tenmin所有資料======================================================================================
        while True:
            sleep(1)
            if waittime=='----':
                waittime='----'
            else:
                timesplit=strftime("%H:%M:%S").split(':')
                second=int(timesplit[0])*3600+int(timesplit[1])*60+int(timesplit[2])
                waittime=second2-second
            print(strftime("%H:%M:%S")+' '+str(waittime)+'s後開始執行')
            
            if strftime("%H:%M:%S") in timelist:#時間檢核!!!
                timeindex=timelist.index(strftime("%H:%M:%S"))#時間位置
                timesplit2=timelist[timeindex+1].split(':')#下一時間位置
                second2=int(timesplit2[0])*3600+int(timesplit2[1])*60+int(timesplit2[2])
                waittime=second2-second
                print('start: '+strftime("%H:%M:%S")+1)
                
                x = datetime.datetime.now()
                day1=x.year
                day2=x.month #會拿到 12
                day3=x.day # 會拿到 5
                day4=x.hour   #時
                day5=x.minute #分
                if day2 < 10: #月
                    day2='0'+str(day2)
                if day3 < 10: #日
                    day3='0'+str(day3)
                if day4 < 10: #時
                    day4='0'+str(day4)
                if day5 < 10: #分
                    day5='0'+str(day5)
                #24小時時間抓取=============================================================
                comptime01=hours(1)
                comptime03=hours(3)
                comptime06=hours(6)
                comptime12=hours(12)
                comptime24=hours(24)
                    
                tenmin=[]
                inttenmin=[]
                chrome = webdriver.Chrome()
                chrome.get('https://www.cwb.gov.tw/V8/C/P/Rainfall/Rainfall_10Min_County.html')
                sleep(2)
                chrome.find_element_by_id('scity').click()
                sleep(2)
                chrome.find_element_by_xpath('/html/body/form/fieldset/div/div/div[2]/label/select/option[10]').click()#彰化
                sleep(2)
                for i in range(len(tenminlist)):
                    try:
                        tenmin.append(chrome.find_element_by_xpath(tenminlist[i]).text)
                    except:
                        tenmin.append('error')
                        print('erroe')
            #資料格式轉換=======================================================================================
                for i in tenmin:
                    if i =='-':
                        inttenmin.append(0)
                    elif i =='error':
                        inttenmin.append(0)
                    elif i =='X':
                        inttenmin.append(0)
                    else:
                        inttenmin.append(float(i))
            #雨量判斷==========================================================================================
                for i in range(len(inttenmin)):
                    if i==len(inttenmin)-1:
                        print('no rain')
                    if inttenmin[i]>=3.0:
                        rain3mm=1
        #                x = datetime.datetime.now()
        #                day1=x.year
        #                day2=x.month #會拿到 12
        #                day3=x.day # 會拿到 5
        #                day4=x.hour   #時
        #                day5=x.minute #分
        #                if day2 < 10: #月
        #                    day2='0'+str(day2)
        #                if day3 < 10: #日
        #                    day3='0'+str(day3)
        #                if day4 < 10: #時
        #                    day4='0'+str(day4)
        #                if day5 < 10: #分
        #                    day5='0'+str(day5)    
                        nowtime=str(day1)+'/'+str(day2)+'/'+str(day3)+' '+str(day4)+':'+str(day5)
                        print(nowtime)
        #                nowtimelist.append(nowtime)
                        beforerainyn=beforerainyn+1
        #                if beforerainyn>=2:
        #                    beforerainyn=2
        #                break
        #        if i==len(inttenmin)-1:
        #            beforerainyn=0
        #            nowtimelist=[]
        #            print('no rain')
        #        if beforerainyn==2: #執行爬蟲程式!!!!!
                        print('look for data')
                        #gerdataimgdict參數重置==================================
                        yn=1
                        allotherlist=[]
                        otherlist=[]
                        alldata=[]
                        initialdata=[]
                        numberlist=[]
                        titlelist=[]
                        dict1={}
                        dict2={}
                        #getdataimgdict程式碼================================
                        chrome.get('https://corsline.ncdr.nat.gov.tw/ncdr/admin/login')
                        chrome.find_element_by_id('account').send_keys('team02')
                        sleep(1)
                        chrome.find_element_by_name('j_password').send_keys('team02')
                        sleep(1)
                        chrome.find_element_by_xpath('//*[@id="loginContainter"]/div[1]/form/div/ul/li[3]/input').click()
                        sleep(1)
                        chrome.get('https://corsline.ncdr.nat.gov.tw/ncdr/admin/manage/line/event/queryList')
                        chrome.find_element_by_id('queryStartTime').clear()
                        chrome.find_element_by_id('queryStartTime').send_keys(str(day1)+'/'+str(day2)+'/'+str(day3)+' '+'00:00')
                        chrome.find_element_by_id('queryEndTime').clear()
                        chrome.find_element_by_id('queryEndTime').send_keys(nowtime)
                        chrome.find_element_by_xpath('//*[@id="searchForm"]/input[3]').click()
                        sleep(2)
                        while yn!=0:
                            for i in range(10):#一頁十筆資料    
                                otherlist=[]
                                try:
                                    numberlist.append(chrome.find_element_by_xpath(xpathlist[i]).text)
                                except:
                                    numberlist.append('error')
                                    print('numbererror')
                                    yn=0
                                    break
                                try:
                                    titlelist.append(chrome.find_element_by_xpath(titlexpathlist[i]).get_attribute('title'))
                                except:
                                    titlelist.append('error')
                                    print('titleerror')
                                    yn=0
                                    break
                                for j in range(9):#每一筆資料除編號、title以外的資料
                                    try:
                                        otherlist.append(chrome.find_element_by_xpath(otherxpathlist[i][j]).text)
                                    except:
                                        otherlist.append('error')
                                        print('othererror')
                                    if j==8:
                                        try:
                                            otherlist.append(chrome.find_element_by_xpath(imglist[i]).get_attribute('src'))
                                        except:
                                            otherlist.append('error')
                                            print('imgerror')
                                    if j==8:
                                        allotherlist.append(otherlist)
                                        
                                if i==9:
                                    try:
                                        chrome. find_element_by_class_name('next').click()
                                        sleep(3)
                                    except:
                                        print('finish get data')
                                        yn=0
                        
                        #開啟excel========================================================================================
                        app = xw.App(visible=True,add_book=False)
                        wb = app.books.add()
                        #wb = xw.Book('initialdataimg.xlsx')
                        sht = wb.sheets[0]                    
                        for j in range(len(titlelist)):
                            if numberlist[0]=='目前無災情通報資訊':
                                #sht.range('a'+str(j+1)).value =numberlist[j]
                                sht.range('a'+str(j+1)).value =""
                                print('目前無災情通報資訊')
                                break
                            sht.range('a'+str(j+1)).value =numberlist[j]
                            sht.range('b'+str(j+1)).value =titlelist[j]
                            sht.range('c'+str(j+1)).value =allotherlist[j][0]
                            sht.range('d'+str(j+1)).value =allotherlist[j][1]
                            sht.range('e'+str(j+1)).value =allotherlist[j][2]
                            sht.range('f'+str(j+1)).value =allotherlist[j][3]
                            sht.range('g'+str(j+1)).value =allotherlist[j][4]
                            sht.range('h'+str(j+1)).value =allotherlist[j][5]
                            sht.range('i'+str(j+1)).value =allotherlist[j][6]
                            sht.range('j'+str(j+1)).value =allotherlist[j][7]
                            sht.range('k'+str(j+1)).value =allotherlist[j][8]
                            sht.range('l'+str(j+1)).value =allotherlist[j][9]
                        
                        #建立字典資料========================================================================================
                        wb2 = xw.Book('namev3.xlsx')
                        sht2 = wb2.sheets[0]
                        rng = sht2.range('a1').expand('table')
                        nrows = rng.rows.count
                        for j in range(nrows):
                            dict1[sht2.range('c'+str(j+1)).value]=sht2.range('e'+str(j+1)).value
                            dict2[sht2.range('c'+str(j+1)).value]=sht2.range('c'+str(j+1)).value
                            dict3[sht2.range('c'+str(j+1)).value]=sht2.range('g'+str(j+1)).value
                        print('finish dict')
                        #字典查詢輸入========================================================================================
                        for i in range(len(titlelist)):
                            if numberlist[0]=='目前無災情通報資訊':
                                print('目前無災情通報資訊')
                                break
                            try:
                                sht.range('m'+str(i+1)).value = dict1[sht.range('b'+str(i+1)).value]
                                sht.range('n'+str(i+1)).value = dict2[sht.range('b'+str(i+1)).value]
                                sht.range('o'+str(i+1)).value = dict3[sht.range('b'+str(i+1)).value]
                            except:
                                sht.range('o'+str(i+1)).value = 'Ot'
        #                        sht.range('m'+str(i+1)).value = 'error'
        #                        sht.range('n'+str(i+1)).value = 'error'
                                print('name error')
                        sleep(2)
                        wb.save('initialdata'+str(day1)+'_'+str(day2)+'_'+str(day3)+'_'+str(day4)+str(day5)+'.xlsx')
                        #刪除initialdata====================================================================================
                        try :
                            sleep(1)
                            os.remove('initialdata.xlsx')
                        except:
                            print('initialdata error')
                        sleep(2)
                        #新建initialdata====================================================================================
                        wb.save('initialdata.xlsx')
                        print('save excel')
                        sleep(1)
                        app.quit()
                        break
                        #print('allfinish')
                        #================================
                
    #            os.system ('GO_ALL.bat')
                chrome.close()
                print('allfinish')
                sleep(1)
                #24小時第二次抓取====================================================================
                #gerdataimgdict參數重置==================================
            if rain3mm==1:
                yn=1
                allotherlist=[]
                otherlist=[]
                alldata=[]
                initialdata=[]
                numberlist=[]
                titlelist=[]
                rain3mm=0
                #getdataimgdict程式碼================================
                chrome = webdriver.Chrome()
                chrome.get('https://corsline.ncdr.nat.gov.tw/ncdr/admin/login')
                chrome.find_element_by_id('account').send_keys('team02')
                sleep(1)
                chrome.find_element_by_name('j_password').send_keys('team02')
                sleep(1)
                chrome.find_element_by_xpath('//*[@id="loginContainter"]/div[1]/form/div/ul/li[3]/input').click()
                sleep(1)
                chrome.get('https://corsline.ncdr.nat.gov.tw/ncdr/admin/manage/line/event/queryList')
                chrome.find_element_by_id('queryStartTime').clear()
                chrome.find_element_by_id('queryStartTime').send_keys(comptime24)
                chrome.find_element_by_id('queryEndTime').clear()
                chrome.find_element_by_id('queryEndTime').send_keys(nowtime)
                chrome.find_element_by_xpath('//*[@id="searchForm"]/input[3]').click()
                sleep(2)
                while yn!=0:
                    for i in range(10):#一頁十筆資料    
                        otherlist=[]
                        try:
                            numberlist.append(chrome.find_element_by_xpath(xpathlist[i]).text)
                        except:
                            numberlist.append('error')
                            print('numbererror')
                            yn=0
                            break
                        try:
                            titlelist.append(chrome.find_element_by_xpath(titlexpathlist[i]).get_attribute('title'))
                        except:
                            titlelist.append('error')
                            print('titleerror')
                            yn=0
                            break
                        for j in range(9):#每一筆資料除編號、title以外的資料
                            try:
                                otherlist.append(chrome.find_element_by_xpath(otherxpathlist[i][j]).text)
                            except:
                                otherlist.append('error')
                                print('othererror')
                            if j==8:
                                try:
                                    otherlist.append(chrome.find_element_by_xpath(imglist[i]).get_attribute('src'))
                                except:
                                    otherlist.append('error')
                                    print('imgerror')
                            if j==8:
                                allotherlist.append(otherlist)
                                
                        if i==9:
                            try:
                                chrome. find_element_by_class_name('next').click()
                                sleep(3)
                            except:
                                print('finish get data')
                                yn=0
                #開啟excel========================================================================================
                app = xw.App(visible=True,add_book=False)
                wb = app.books.add()
                #wb = xw.Book('initialdataimg.xlsx')
                sht = wb.sheets[0]                    
                for j in range(len(titlelist)):
                    if numberlist[0]=='目前無災情通報資訊':
                        #sht.range('a'+str(j+1)).value =numberlist[j]
                        sht.range('a'+str(j+1)).value =""
                        print('目前無災情通報資訊')
                        break
                    sht.range('a'+str(j+1)).value =numberlist[j]
                    sht.range('b'+str(j+1)).value =titlelist[j]
                    sht.range('c'+str(j+1)).value =allotherlist[j][0]
                    sht.range('d'+str(j+1)).value =allotherlist[j][1]
                    sht.range('e'+str(j+1)).value =allotherlist[j][2]
                    sht.range('f'+str(j+1)).value =allotherlist[j][3]
                    sht.range('g'+str(j+1)).value =allotherlist[j][4]
                    sht.range('h'+str(j+1)).value =allotherlist[j][5]
                    sht.range('i'+str(j+1)).value =allotherlist[j][6]
                    sht.range('j'+str(j+1)).value =allotherlist[j][7]
                    sht.range('k'+str(j+1)).value =allotherlist[j][8]
                    sht.range('l'+str(j+1)).value =allotherlist[j][9]
             #字典查詢輸入========================================================================================
                for i in range(len(titlelist)):
                    if numberlist[0]=='目前無災情通報資訊':
                        print('24目前無災情通報資訊')
                        break
                    try:
                        sht.range('m'+str(i+1)).value = dict1[sht.range('b'+str(i+1)).value]
                        sht.range('n'+str(i+1)).value = dict2[sht.range('b'+str(i+1)).value]
                        sht.range('o'+str(i+1)).value = dict3[sht.range('b'+str(i+1)).value]
                    except:
                        sht.range('o'+str(i+1)).value = 'Ot'
    #                        sht.range('m'+str(i+1)).value = 'error'
    #                        sht.range('n'+str(i+1)).value = 'error'
                        print('24name error')
                sleep(2)
                wb.save('initialdata'+str(day1)+'_'+str(day2)+'_'+str(day3)+'_'+str(day4)+str(day5)+'.xlsx')
                #刪除initialdata====================================================================================
                try :
                    sleep(1)
                    os.remove('initialdata24.xlsx')
                except:
                    print('initialdata24 error')
                sleep(2)
                #新建initialdata====================================================================================
                wb.save('initialdata24.xlsx')
                print('24save excel')
                sleep(1)
                app.quit()
                chrome.close()
                sleep(1)
                #比較01、03、06、12小時excel資料================================================
                excel24(comptime01,'01')
                excel24(comptime03,'03')
                excel24(comptime06,'06')
                excel24(comptime12,'12')
                
                os.system ('GO_ALL.bat')
                
    
                checktime=checktime+1
                print('finish check'+str(checktime))
                sleep(10)#tenmin間格 
    except:    
        print('all out')
        traceback.print_exc()
        lineNotifyMessage('Gl1uixokULB91nXRrqVlXBXojcomOJ0hfeTuzFTxcbq', message)
        lineNotifyMessage('Gl1uixokULB91nXRrqVlXBXojcomOJ0hfeTuzFTxcbq', traceback.print_exc())
        lineNotifyMessage('A8awq49cUUIt2LnFsE28ZJpRDmQ0uhM25pEXd80iTgl', message)
        lineNotifyMessage('A8awq49cUUIt2LnFsE28ZJpRDmQ0uhM25pEXd80iTgl', traceback.print_exc())
    
    sleep(5)
    continue
    
    
















