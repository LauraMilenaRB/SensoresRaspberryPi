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

def DHT11(sensor, pin):
    
    while True:
        temp, hum = Adafruit_DHT.read_retry(sensor, pin)
        data[0]=round(temp,1)
        data[1]=round(hum,1)
        RestRequests()
        time.sleep(5)
    
    
def RestRequests():
    
    # Definimos la URL
    url = "https://192.168.0.15/"
    # Solicitamos los datos del usuario
    # Definimos la cabecera y el diccionario con los datos
    header = {'Content-type': 'application/json'}
    dat = ('User:{"email": "%s","password":"%s","name":"%s","image":"%s","confirmPassword":"%s"}')%("email","pdw", "name","image","pdw")
    petition = requests.post(url+"/users/", headers = header, data = dat)
    if petition.status_code == 200:
        print(petition.text)
        
def main():
    t = threading.Thread(target=DHT11(11,2))
    t.start()
    if __name__:"main"

