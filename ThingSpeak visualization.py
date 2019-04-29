# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:36:12 2019

@author: Home
"""

import requests as r

def send_data(temperatureList):    
    url = 'https://api.thingspeak.com/channels/XXXXXX/bulk_update.json' #write your TS channel number
    
    data = {
    	"write_api_key": "", #Your API key
    	"updates": temperatureList}  
    
    resp = r.post(url, json=data)
    
    print("Status: ", resp.status_code)