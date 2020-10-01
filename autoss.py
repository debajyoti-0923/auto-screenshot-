import pyautogui as pg
import os
import time
from pynput.mouse import Listener
from math import floor
import sys
from datetime import datetime
import keyboard
from pynput import keyboard as k2


f=0
sc=0
date=datetime.now().strftime('%d.%m.%Y')

def rai():
    global f
    f+=1

keyboard.add_hotkey('ctrl+shift+/',lambda:rai())





def onclick(x, y, button, pressed):
    global a
    global b
    if pressed:
        a=(x,y)
    else:
        b=(x,y)
    if not pressed:
        return False

def fti():
    ti=pg.prompt('Enter interval time(in seconds):','AutoSS','180')
    if ti==None:
        qu=pg.confirm('You want to exit?"','AutoSS',buttons=('Yes','No'))
        if qu=='Yes':
            sys.exit(0)
        else:
            ti=pg.prompt('Enter interval time(in seconds):','AutoSS','180')
            if ti==None:
                sys.exit(0)
    try:
        ti=int(ti)
    except:
        pg.alert('Input not recognized','AutoSS')
        sys.exit(0)
    return ti

def fton():  
    ton=pg.prompt('Enter total on time(in minutes):','AutoSS','60')
    if ton==None:
        qu=pg.confirm('You want to exit?"','AutoSS',buttons=('Yes','No'))
        if qu=='Yes':
            sys.exit(0)
        else:
            ton=pg.prompt('Enter interval time(in seconds):','AutoSS','60')
            if ton==None:
                sys.exit(0)
    try:
        ton=float(ton)
    except:
        pg.alert('Input not recognized','AutoSS')
        sys.exit(0)
    return ton

def po(ton,ti):
    global sc
    p=(floor(float(ton)*60))//int(ti)
    sc=p
    return p

def size():
    ss=pg.confirm('Screen Space','Auto SS',buttons=('Full Screen','Custom'))
    if ss=='Full Screen':
        l,t,w,h=0,0,1599,899
    else:
        z=pg.confirm('Select the SS area by click and hold.\n(Going Up to Down!!)','AutoSS')
        if z=='OK':       
            with Listener(on_click=onclick) as listener:
                listener.join()
            l,t=a[0],a[1]
            if b[0]>a[0]:
                w=b[0]-a[0]
            else:
                w=a[0]-b[0]
            if b[1]>a[1]:
                h=b[1]-a[1]
            else:
                h=a[1]-b[1]
        else:
            pg.alert('"CANCEL" detected, set full screenshot!','AutoSS')
            l,t,w,h=0,0,1599,899
    return l,t,w,h

def store(date):
    dloc="H:/AutoSS data/"
    loc=pg.confirm('{}\n\nConfirm saving location.'.format(dloc),'AutoSS',buttons=('OK','NO'))
    if loc=='OK':
        loc=dloc
    else:
        while loc in ['NO',None]:
            loc=pg.prompt('Enter new path:','Auto SS',"H:/AutoSS data/")   
    try:
        path=loc+date
        os.mkdir(path)
        loc=path
    except:
        loc=loc+date
    return loc


def on_press(key,end=''):
    global pa
    global wh
    pa=0
    pr=key.char
    if pr=='c' or pr=='C':
        pa+=1
        return False
    if pr=='e' or pr=='E':
        wh=False
        return  False
ti=fti()
ton=fton()
p=po(ton,ti)
l,t,w,h=size()
loc=store(date)
    
imin=int(datetime.now().strftime('%M'))*60
inow=imin
def eff(l,t,w,h,loc,ti):
    global imin
    global f
    global inow
    global p
    global ton
    global sc
    global pa
    global wh
    de={}
    dek=0
    z=0
    ac=0
    while True:
        if f==0:
            inow+=1
            time.sleep(1)
            if ac>0:
                #print('pl',inow,du)
                if inow==du:
                    ac=0
                    #print(ac)
                    for i in de.values():
                        x,y=i
                        pg.click(x,y)
                    de={}
            if inow-1==imin:
                imin+=ti
                if z>0:
                    os.remove(floc)
                    z=0
                try:
                    #print(p)
                    im1 = pg.screenshot(region=(l,t,w,h))
                    times=datetime.now().strftime('%H.%M')
                    floc=loc+"\\{0}ss{1}.png".format(date,times)
                    im1.save(floc)
                    z+=1
                    p-=1
                    if p==0:
                        #print(p)
                        pg.alert('Task ending.\nThank You!','AutoSS')
                        break
                except:
                    pg.alert('Screenshot cant be saved: Storage location not found','AutoSS')
        else:
            c=pg.confirm('AutoSS paused','AutoSS',buttons=('Resume','Show details','Reset interval time','Reset ON_time','Reconfigure size','Reconfigure Path','clk sc','End'))
            if c=='Resume':
                f-=1
            elif c=='Reset interval time':
                imin=imin-ti
                ti=fti()
                imin=imin+ti
                p=po(ton,ti)
                f-=1
            elif c=='Reset ON_time':
                ton=fton()
                p=po(ton,ti)
                f-=1
            elif c=='Reconfigure size':
                l,t,w,h=size()
                f-=1
            elif c=='Reconfigure Path':
                loc=store(date)
                f-=1
            elif c=='Show details':
                pg.alert('Screenshots taken:{0}\n\nInterval time:{1}(Seconds)\n\nTotal ON time:{2}(Minutes)\n\nTime remaining:{3}(approx)\n\nWindow size={4}*{5}\n\nLocation:{6}'.format(sc-p,ti,ton,ton-(((sc-p)*ti)//60),h,w,loc),'AutoSS')
                f-=1
            elif c=='clk sc':
                ac+=1
                pg.alert('Move pointer to the postion where you want to click and press \'c\' to record and \'e\' to end recoring.','AutoSS')
                wh=True
                while wh==True :
                    with k2.Listener(on_press=on_press) as listener:
                        listener.join()
                    if pa==1:
                        [q,wt]=pg.position()
                        de[dek]=[q,wt]
                        dek+=1
                        pa-=1
                du=pg.prompt('Minutes from Now=','AutoSS')
                du=inow+(float(du)*60)
                f-=1
                #print(de)
            elif c is None:
                f-=1
            else:
                pg.alert('Thank you!','AutoSS')
                break


    
def noneff(l,t,w,h,loc,ti):
    global imin
    global f
    global inow
    global p
    global ton
    global sc
    global pa
    global wh
    de={}
    dek=0
    ac=0
    while True:
        if f==0:
            inow+=1
            time.sleep(1)
            if ac>0:
                #print('pl',inow,du)
                if inow==du:
                    ac=0
                    #print(ac)
                    for i in de.values():
                        x,y=i
                        pg.click(x,y)
                    de={}
            if inow-1==imin:
                imin+=ti
                try:
                    #print(p)
                    im1 = pg.screenshot(region=(l,t,w,h))
                    times=datetime.now().strftime('%H.%M')
                    floc=loc+"\\{0}ss{1}.png".format(date,times)
                    im1.save(floc)
                    p-=1
                    if p==0:
                        #print(p)
                        pg.alert('Task ending.\nThank You!','AutoSS')
                        break
                except:
                    pg.alert('Screenshot cant be saved: Storage location not found','AutoSS')
        else:
            c=pg.confirm('AutoSS paused','AutoSS',buttons=('Resume','Show details','Reset interval time','Reset ON_time','Reconfigure size','Reconfigure Path','clk sc','End'))
            if c=='Resume':
                f-=1
            elif c=='Reset interval time':
                imin=imin-ti
                ti=fti()
                imin=imin+ti
                p=po(ton,ti)
                f-=1
            elif c=='Reset ON_time':
                ton=fton()
                p=po(ton,ti)
                f-=1
            elif c=='Reconfigure size':
                l,t,w,h=size()
                f-=1
            elif c=='Reconfigure Path':
                loc=store(date)
                f-=1
            elif c=='Show details':
                pg.alert('Screenshots taken:{0}\n\nInterval time:{1}(Seconds)\n\nTotal ON time:{2}(Minutes)\n\nTime remaining:{3}(approx)\n\nWindow size={4}*{5}\n\nLocation:{6}'.format(sc-p,ti,ton,ton-(((sc-p)*ti)//60),h,w,loc),'AutoSS')
                f-=1
            elif c=='clk sc':
                ac+=1
                pg.alert('Move pointer to the postion where you want to click and press \'c\' to record and \'e\' to end recoring.','AutoSS')
                wh=True
                while wh==True :
                    with k2.Listener(on_press=on_press) as listener:
                        listener.join()
                    if pa==1:
                        [q,wt]=pg.position()
                        de[dek]=[q,wt]
                        dek+=1
                        pa-=1
                du=pg.prompt('Minutes from Now=','AutoSS')
                du=inow+(float(du)*60)
                f-=1
                #print(de)
            elif c is None:
                f-=1
            else:
                pg.alert('Thank you!','AutoSS')
                break

co=pg.confirm('Confirm function:\n\nSpace efficient: Upload to Drive and Delete.\n\nNon efficient: Upload to drive dont Delete.','Auto SS',buttons=('Non efficient','Space efficient')) 



if co=='Space efficient':
    pg.alert('Make sure you have good internet connection','AutoSS')
    
    eff(l,t,w,h,loc,ti)
else:
    pg.alert('Make sure you have good internet connection','AutoSS')
    noneff(l,t,w,h,loc,ti)






