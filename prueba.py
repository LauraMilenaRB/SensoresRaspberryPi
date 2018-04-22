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
        if(temp!=data[0] or hum!=data[1]):
            data[0]=str(float(round(temp,1)))
            data[1]=str(float(round(hum,1)))
            RestRequestsDHT()
        time.sleep(12)
        
def Water(pin):
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.IN)
    try:
        while True:
            state=gpio.input(pin)
            if((data[2]=="true" and state==1) or (data[2]=="true" and state==0)):
                if not(gpio.input(pin)):
                    data[2]="true"
                else:
                    data[2]="false"
                RestRequestsWater()
            time.sleep(8)
    finally:
        gpio.cleanup()
        
def Temperature(pin):
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.IN)
    try:
        while True:
            if (gpio.input(pin)==0):
                data[3]="false"
                print("temp")
            RestRequestsTemp()

    finally:
        gpio.cleanup()
        
def RestRequestsDHT():
    petition = requests.post(url+"DHT/"+data[0]+"&"+data[1])
    if petition.status_code == 200:
        print(petition.text)
        
def RestRequestsWater():
    petition = requests.post(url+"water/"+data[2])
    if petition.status_code == 200:
        print(petition.text)
        
def RestRequestsTemp():
    petition = requests.post(url+"temperature/"+data[3])
    if petition.status_code == 200:
        print(petition.text)
        
def main():
    tempHum = threading.Thread(target=DHT,args=(Adafruit_DHT.DHT11,2,))
    rain= threading.Thread(target=Water,args=(3,))
    temp= threading.Thread(target=Temperature,args=(4,))
    tempHum.start()
    rain.start()
    temp.start()
    if __name__:"main"

