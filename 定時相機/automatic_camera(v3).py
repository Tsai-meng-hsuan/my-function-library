# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:41:25 2021

@author: user
"""

import cv2
import datetime
from time import strftime

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
    hours=str(day1)+'_'+str(day2)+'_'+str(day3)+'_'+str(day4)+str(day5)
    return hours

def ttmin(T):
    x =datetime.datetime.now()+datetime.timedelta(hours=-T)
    day1=x.year
    day2=x.month #會拿到 12
    day3=x.day # 會拿到 5
    day4=x.hour   #時
    day5=x.minute #分
    ttmin=day4*60+day5
    return ttmin

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
          '23:02:00','23:12:00','23:22:00','23:32:00','23:42:00','23:52:00'
          ]

n=0

# 選擇第二隻攝影機
cap0 = cv2.VideoCapture(0)
cap0.set(3, 720)
cap0.set(4, 480)

cap1 = cv2.VideoCapture(1)
cap1.set(3, 720)
cap1.set(4, 480)

before_time=strftime("%H:%M:%S")
before_ttmin=ttmin(24)
now_ttmin=ttmin(24)
while(True):
  later_ttmin=ttmin(24)
  if later_ttmin != before_ttmin:
    before_ttmin = later_ttmin
    n=n+1
    print(before_ttmin)
    print('n= ',n)
    
  later_time=strftime("%H:%M:%S")
  if before_time != later_time:
    before_time = later_time
    print(before_time)
    
    
    # 從攝影機擷取一張影像
  ret0, frame0 = cap0.read()
  ret1, frame1 = cap1.read()

  # 顯示圖片
  cv2.imshow('frame0', frame0)
  cv2.imshow('frame1', frame1)
  
  
  # if strftime("%H:%M:%S") in timelist:#時間檢核!!!
  #   cv2.imwrite('cap0_'+hours(24)+'.png', frame0)
  #   cv2.imwrite('cap1_'+hours(24)+'.png', frame1)
  #   print("take picture!!")
  if n <= 1440 :
    time_difference=60
    if n <= 480 :
        time_difference=30
        if n <= 240:
            time_difference=10
            if n <= 60:
                time_difference=3
                if n <= 30:
                    time_difference=1
  if n >1440:
     time_difference=120 
    
  if before_ttmin-now_ttmin == time_difference :
    cv2.imwrite('cap0_'+hours(24)+'.png', frame0)
    cv2.imwrite('cap1_'+hours(24)+'.png', frame1)
    print("take picture!!")
    now_ttmin=before_ttmin
  

  if cv2.waitKey(1) & 0xFF == ord('d'):
    cv2.imwrite('cap0_'+hours(24)+'_'+str(n)+'.png', frame0)
    cv2.imwrite('cap1_'+hours(24)+'_'+str(n)+'.png', frame1)
    print("take picture!!")
  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    print('stop!!')
    break

# 釋放攝影機
cap0.release()
cap1.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()