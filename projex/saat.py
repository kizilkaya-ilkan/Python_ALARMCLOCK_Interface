from tkinter import *
import tkinter as tk
import time
import datetime
# pip install pygame 
# pip install mixer
# pip install python-vlc
import pygame
import mixer
import time
import vlc
saat1 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat1.mp3")
saat12 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat12.mp3")
saat2 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat2.mp3")
saat3 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat3.mp3")
saat4 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat4.mp3")
saat5 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat5.mp3")
saat6 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat6.mp3")
saat7 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat7.mp3")
saat8 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat8.mp3")
saat9 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat9.mp3")
saat10 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat10.mp3")
saat11 = vlc.MediaPlayer("C:/Users/Huawei/OneDrive/Masaüstü/projex/saat11.mp3")
pencere = tk.Tk()
pencere.title("Saat")
pencere.geometry("200x80+50+100")
zaman1=''
etiket1=tk.Label(pencere,text="Saat Uygulaması")
etiket1.pack()
tiktak1 = tk.Label(pencere , font=('times',20,'bold',), bg='pink')
tiktak1.pack()

def saat():
        global zaman1
        global now
        zaman2 = time.strftime('%H:%M:%S')
        if zaman2 != zaman1:
                zaman1=zaman2
                tiktak1.config(text=zaman2)
                an = datetime.datetime.now()
                now = an
        tiktak1.after(50, saat)
        
        if now.hour == 12 and now.minute == 0 and now.second == 0:
                saat12.play()
                time.sleep(5)
                saat12.stop() 
        if now.hour == 13 and now.minute == 0 and now.second == 0:
                saat1.play()
                time.sleep(5)
                saat1.stop() 
        if now.hour == 14 and now.minute == 0 and now.second == 0:
                saat2.play()
                time.sleep(5)
                saat2.stop()           
        if now.hour == 15 and now.minute == 0 and now.second == 0:
               saat3.play()
               time.sleep(5)
               saat3.stop()          
        if now.hour == 16 and now.minute == 0 and now.second == 0:
                saat4.play()
                time.sleep(5)
                saat4.stop()              
        if now.hour == 17 and now.minute == 0 and now.second == 0:
               saat5.play()
               time.sleep(5)
               saat5.stop()              
        if now.hour == 18 and now.minute == 0 and now.second == 0:
               saat6.play()
               time.sleep(5)
               saat6.stop()           
        if now.hour == 19 and now.minute == 0 and now.second == 0:
               saat7.play()
               time.sleep(5)
               saat7.stop()   
        if now.hour == 20 and now.minute == 0 and now.second == 0:
               saat8.play()
               time.sleep(5)
               saat8.stop()   
        if now.hour == 21 and now.minute == 0 and now.second == 0:
               saat9.play()
               time.sleep(5)
               saat9.stop()                      
        if now.hour == 22 and now.minute == 0 and now.second == 0:
               saat10.play()
               time.sleep(5)
               saat10.stop()                     
        if now.hour == 23 and now.minute == 0 and now.second == 0:
               saat11.play()
               time.sleep(5)
               saat11.stop()                     
        if now.hour == 00 and now.minute == 0 and now.second == 0:
                saat12.play()
                time.sleep(5)
                saat12.stop()                    
        if now.hour == 1 and now.minute == 0 and now.second == 0:
               saat1.play()
               time.sleep(5)
               saat1.stop()
        if now.hour == 2 and now.minute == 0 and now.second == 0:
                saat2.play()
                time.sleep(5)
                saat2.stop()          
        if now.hour == 3 and now.minute == 0 and now.second == 0:
                saat3.play()
                time.sleep(5)
                saat3.stop()               
        if now.hour == 4 and now.minute == 0 and now.second == 0:
                saat4.play()
                time.sleep(5)
                saat4.stop()                    
        if now.hour == 5 and now.minute == 0 and now.second == 0: 
                saat5.play()
                time.sleep(5)
                saat5.stop()                 
        if now.hour == 6 and now.minute == 0 and now.second == 0:
                saat6.play()
                time.sleep(5)
                saat6.stop()                       
        if now.hour == 7 and now.minute == 0 and now.second == 0:
                saat7.play()
                time.sleep(5)
                saat7.stop()                   
        if now.hour == 8 and now.minute == 0 and now.second == 0:
                saat8.play()
                time.sleep(5)
                saat8.stop()                      
        if now.hour == 9 and now.minute == 0 and now.second == 0:
                saat9.play()
                time.sleep(5)
                saat9.stop()                   
        if now.hour == 10 and now.minute == 0 and now.second == 0:
                saat10.play()
                time.sleep(5)
                saat10.stop()                     
        if now.hour == 11 and now.minute == 0 and now.second == 0:
                saat11.play()
                time.sleep(5)
                saat11.stop()                    
        
saat()
pencere.mainloop(  )
