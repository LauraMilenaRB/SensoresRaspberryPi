# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import Adafruit_DHT
import requests
import threading
import time
    
data=[1,2,3,4]

def DHT(sensor, pin):
    
    while True:
        temp, hum = Adafruit_DHT.read_retry(sensor, pin)
        data[0]=round(temp,1)
        data[1]=round(hum,1)
        RestRequests()
        time.sleep(10)
    
    
def RestRequests():
    
    # URL
    url = "http://192.168.0.15:8080/"
    header = {'Content-type': 'application/json'}

    #Data
    petition = requests.post(url+"sensores/DHT/"data[0]+"&"+data[1])
    if petition.status_code == 200:
        print(petition.text)
        
    #Data
    #dat = ('{"temp": "%s","humedad":"%s"}')%(data[0],data[1])
    #petition = requests.post(url+"sensores/", headers = header, data = dat)
    #if petition.status_code == 200:
        #print(petition.text)
        
def main():
    t = threading.Thread(target=DHT,args=(Adafruit_DHT.DHT11,2))
    t.start()
    if __name__:"main"

