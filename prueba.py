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
        print(temp,hum)
        RestRequests()
        break
    
    
def RestRequests():
    
    # Definimos la URL
    url = "https://192.168.0.15/"
    header = {'Content-type': 'application/json'}
    dat = ('{"email": "%s","password":"%s","name":"%s","image":"%s","confirmPassword":"%s"}')%("email","pdw", "name","image","pdw")
    print("mdfknfoindiofnvfr")
    petition = requests.post(url+"users/", headers = header, data = dat)
    print("mdfknfoindiofnvfr2")
    if petition.status_code == 200:
        print(petition.text)
    print("mdfknfoindiofnvfr3")
        
def main():
    t = threading.Thread(target=DHT,args=(Adafruit_DHT.DHT11,2))
    t.start()
    if __name__:"main"

