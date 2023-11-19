# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:35:43 2018

@author: memgal
"""

from time import sleep
from time import strftime
from time import time
from selenium import webdriver
import requests
import hashlib
import os
from selenium.common.exceptions import NoSuchElementException

print('==========login2.ver3.5.2==========')
x=0
n=1
a1=input('輸入使用者學號: ')
while a1==(''):
    print('未輸入')
    print('-----------------')
    a1=input('輸入使用者學號: ')
a2=input('輸入使用者密碼: ')
while a2==(''):
    print('未輸入')
    print('-----------------')
    a2=input('輸入使用者密碼: ')
b=input('輸入學號2: ')
while b==(''):
    print('未輸入')
    print('-----------------')
    b=input('輸入學號2: ')
c=input('輸入學號3: ')
while c==(''):
    print('未輸入')
    print('-----------------')
    c=input('輸入學號3: ')
d=input('輸入學號4: ')
while d==(''):
    print('未輸入')
    print('-----------------')
    d=input('輸入學號4: ')

B=input('輸入日期: ')
while B==(''):
    print('未輸入')
    print('-----------------')
    B=input('輸入日期: ')
A="//option[@value='"
C="']"
date=A+B+C
print(date)

DCtime=int(input('輸入時段(2~4): '))
place=int(input('輸入場地(5~12): '))


print('=====================')
print('---please check on---')
print('使用者：'+a1)
print('學號2: '+b)
print('學號3: '+c)
print('學號4: '+d)
print('日期: '+date)
print('時段(2~4): ',DCtime)
print('場地(5~12): ',place)
print('執行時間: 23:30:00')
print('----------------------')
ha=input('確認按enter/錯誤請重新開啟檔案')

if a1==b or a1==c or a1==d or b==c or b==d or c==d :
        print('------------------')
        print('  *警告*  學號重複')
        print('使用者：'+a1)
        print('學號2: '+b)
        print('學號3: '+c)
        print('學號4: '+d)
        print('-------------------')
        ha=input('**請重新開啟檔案**')
        

print('-----------------')        
print('執行中請稍後......') 

chrome = webdriver.Chrome()
chrome.get('http://rent.sim.nchu.edu.tw/index.php')
chrome.set_window_size(600,800)
chrome.find_element_by_name('account').send_keys(a1)
sleep(1)
chrome.find_element_by_name('pwd').send_keys(a2)
sleep(1)
chrome.find_element_by_name('login').click()
chrome.get('http://rent.sim.nchu.edu.tw/index.php?module=rent_pro')

https='http://rent.sim.nchu.edu.tw/index.php?module=rent_pro'
html=requests.get(https).text.encode('utf-8-sig')
md5=hashlib.md5(html).hexdigest()
with open ('oldmd5.txt','w') as f:
            f.write(md5)

while x==0:
    chrome.find_element_by_name('date').click()
    https='http://rent.sim.nchu.edu.tw/index.php?module=rent_pro'
    html=requests.get(https).text.encode('utf-8-sig')
    md5=hashlib.md5(html).hexdigest()
    if os.path.exists('oldmd5.txt'):
        with open('oldmd5.txt','r') as f:
            oldmd5=f.read()
        with open ('oldmd5.txt','w') as f:
            f.write(md5)
    else :
        with open ('oldmd5.txt','w') as f :
            f.write(md5)
    if oldmd5 == md5 :
        print('----------------')
        print('-----已更新-----')
        print('----------------')
        print('newhtml',md5)
        print('oldhtml',oldmd5)
        break
    else :
        print('未更新',n)
        print(oldmd5)
        n=n+1
        sleep(1)
        chrome.refresh()
sleep(1)
chrome.maximize_window()
chrome.find_element_by_xpath("//option[@value='羽球場']").click()
chrome.find_element_by_xpath(date).click()
chrome.find_element_by_xpath("//input[@type='submit']").click()
xpaths=[['//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[6]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[7]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[8]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[9]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[10]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[11]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[12]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td[13]/a/table/tbody/tr/td[1]/img'],
        ['//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[6]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[7]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[8]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[9]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[10]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[11]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[12]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[13]/a/table/tbody/tr/td[1]/img'],
        ['//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[6]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[7]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[8]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[9]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[10]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[11]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[12]/a/table/tbody/tr/td[1]/img',
        '//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[5]/td[13]/a/table/tbody/tr/td[1]/img']]


tStart=time()

refreshtimes=0
while 1:
    try:
        chrome.find_element_by_xpath(xpaths[DCtime-2][place-5]).click()
        try:
            chrome.find_element_by_id('people4').click()
            break
        except:
            place=place+1
            if place==13 :
                place=5
                DCtime=DCtime+1
                if DCtime==5 :
                    DCtime=1
            print('time:',DCtime,'place:',place)
            chrome.get('http://rent.sim.nchu.edu.tw/index.php?module=rent_pro')
            chrome.find_element_by_xpath("//option[@value='羽球場']").click()
            chrome.find_element_by_xpath(date).click()
            chrome.find_element_by_xpath("//input[@type='submit']").click()
            continue
    except NoSuchElementException :
        place=place+1
        if place==13 :
            place=5
            DCtime=DCtime+1
            if DCtime==5 :
                DCtime=1
        print('time:',DCtime,'place:',place)
        refreshtimes=refreshtimes+1
        if refreshtimes==65:
            print('error: no site')
            break
        chrome.refresh()
        continue
    
tEnd=time()
print('out of the loop ,spend time: ',tEnd-tStart)

chrome.find_element_by_name('stdnum2').send_keys(b)
chrome.find_element_by_name('stdnum3').send_keys(c)
chrome.find_element_by_name('stdnum4').send_keys(d)

chrome.find_element_by_name('save').click()

print('Successfully Borrow the site: ',DCtime,'-',place)