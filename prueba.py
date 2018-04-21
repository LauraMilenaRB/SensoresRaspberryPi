# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import Adafruit_DHT
import requests
import threading
import time
    
    
def DHT11():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print ('Temp: {0:01f} C  Humidity: {1:01f} %').format(temperature, humidity)
        time.sleep(1000)
    
    
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
    t = threading.Thread(target=DHT11)
    t.start()
    if __name__:"main"

