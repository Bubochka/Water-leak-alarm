# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:27:07 2019

@author: Home
"""

import os
import time
import smtplib
import ThingSpeak

 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
while True:
    time.sleep(30)    
    try:
# Åbner fil med vores sensor
        tfile=open("/sys/bus/w1/devices/28-00000aca2a9a/w1_slave")
#Læser text i fillen
        ttext=tfile.read()
        tfile.close()
#Spliter teksten med nye linjer (\ n) og vælger den anden linje.Spliter linjen i ord, henviser til mellemrummet, og vælger det 10(tiende) ord (tæller fra 0).
        temp=ttext.split("\n")[1].split(" ")[9]
        temperaturvarmt=float(temp[2:])/1000
        print(temperaturvarmt)
        temperaturList = []
        
        if temperaturvarmt >=23:
            print("Warning, varmt vand spild!!!")
            email_user = '@gmail.com'
            email_password = ''
            email_send = '@gmail.com'
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)
            
            message = 'temperaturen er for hoj'
            
            server.sendmail(email_user,email_send,message)
            server.quit()

        tfile=open("/sys/bus/w1/devices/28-00000aca32e4/w1_slave")
        ttext=tfile.read()
        tfile.close()
        temp=ttext.split("\n")[1].split(" ")[9]
        temperaturkold=float(temp[2:])/1000
        print(temperaturkold)
                 
        if temperaturkold <=22:
            print("Warning, varmt vand spild!!!")
            email_user = '@gmail.com'
            email_password = ''
            email_send = '@gmail.com'
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)
            
            message = 'Temperaturen er for lav'
            
            server.sendmail(email_user,email_send,message)
            server.quit()
               
            
        tfile=open("/sys/bus/w1/devices/28-00000aca43a8/w1_slave")
        ttext=tfile.read()
        tfile.close()
        temp=ttext.split("\n")[1].split(" ")[9]
        stuetemperatur=float(temp[2:])/1000
        print(stuetemperatur)
                
        temperaturList.append({"delta_t" : 1,
                               "field1": temperaturvarmt,
                               "field2": temperaturkold,
                               "field3": stuetemperatur}) 
        ThingSpeak.send_data(temperaturList)
    
    except KeyboardInterrupt:
        print("press control+C again to quit")
    finally:
        print(temperaturvarmt,temperaturkold,stuetemperatur)