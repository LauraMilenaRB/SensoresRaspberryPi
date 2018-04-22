# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import Adafruit_DHT
import requests
import threading
import time
import RPi.GPIO as gpio

    
data=[1,2,3,4]
url = "http://192.168.0.15:8080/sensors/"
def DHT(sensor, pin):
    
    while True:
        temp, hum = Adafruit_DHT.read_retry(sensor, pin)
        data[0]=round(temp,1)
        data[1]=round(hum,1)
        RestRequestsDHT()
        time.sleep(15)
        
def Water(pin):
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.IN)
    try:
        while True:
            state=bool(gpio.input(pin))
            if (not(state)):
                data[2]=state
                RestRequestsWater()
                print("rain")
    finally:
        gpio.cleanup()
        
def RestRequestsDHT():
    petition = requests.post(url+"DHT/"+str(data[0])+"&"+str(data[1]))
    if petition.status_code == 200:
        print(petition.text)
        
def RestRequestsWater():
    petition = requests.post(url+"water/"+str(data[2]))
    if petition.status_code == 200:
        print(petition.text)
        
def main():
    t = threading.Thread(target=DHT,args=(Adafruit_DHT.DHT11,2))
    t2= threading.Thread(target=Water,args=(3))
    t.start()
    t2.start()
    if __name__:"main"

