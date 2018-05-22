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
import socket
import spidev
import geocoder
    
data=["","","",""]
g=geocoder.ip('me')
url = "http://35.166.65.91:8080/sensors/"
ip=socket.gethostbyname(socket.gethostname())+"01"
def DHT(sensor, pin):
    while True:
        temp,hum = Adafruit_DHT.read_retry(sensor, pin)
        if(str(temp)!=data[0] or str(hum)!=data[1]):
            data[0]=str(temp)
            data[1]=str(hum)
            RestRequestsDHT()
        time.sleep(12)
        
def Water(pin):
    gpio.setmode(gpio.BCM)
    gpio.setup(pin,gpio.IN)
    try:
        while True:
            state=gpio.input(pin)
            if((data[2]=="true" and state==1) or (data[2]=="false" and state==0) or (data[2]=="")):
                if not(gpio.input(pin)):
                    data[2]="true"
                else:
                    data[2]="false"
                RestRequestsWater()
            time.sleep(5)
    finally:
        gpio.cleanup()
        
def Temperature(pin):
    '''gpio.setmode(gpio.BCM)
    gpio.setup(pin,gpio.IN)
    try:
        while True:
            if (gpio.input(pin)==0):
                data[3]="false"
            print("temp",gpio.input(pin))
            RestRequestsTemp();time.sleep(12)

    finally:
        gpio.cleanup()'''
    analogPin = pin # A0 connected to A0
    digitalPin = 16 # D0 connected to A1 - not needed
    
    spi = spidev.SpiDev()
    spi.open(0,0)
    
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(digitalPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    
    def readadc(adcnum):
    	# read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
    	if ((adcnum > 3) or (adcnum < 0)):
    		return-1
    	r = spi.xfer2([1,8+adcnum <<4,0])
    	#print(r)
    	adcout = ((r[1] &3) <<8)+r[2]
    	return adcout
    
    tolerance = 0.5 # degrees
    value = readadc(analogPin)
    # calibrate the formula with a termometer
    lasttemp = 125.315 - 0.175529 * value # formula made through Wolfram Alpha: 'linear function (0,125);(720,0);(1023,-55)', where (readvalue, temperature)
    print('Temperature: %5.2f' % lasttemp)
    while True:
    	value = readadc(analogPin)
    	digital = gpio.input(digitalPin)
    	temp = 125.315 - 0.175529 * value
    	if ((temp > lasttemp + tolerance) or (temp < lasttemp - tolerance)): # if temperature changed more than the tolerance
    		print('New temperature: %5.2fC (input: a: %3d, d: %3d)' % (temp, value, digital))
    		lasttemp = temp
    	time.sleep(0.1)
    
    print('done.')
def RestRequestsDHT():
    petition = requests.post(url+"DHT/"+ip+"/"+str(g.lat)+"&"+str(g.lng)+"/"+data[0]+"&"+data[1])
    if petition.status_code == 200:
        print(petition.text)
        
def RestRequestsWater():
    petition = requests.post(url+"water/"+ip+"/"+str(g.lat)+"&"+str(g.lng)+"/"+data[2])
    if petition.status_code == 200:
        print(petition.text)
        
def RestRequestsTemp():
    petition = requests.post(url+"temperature/"+ip+"/"+str(g.lat)+"&"+str(g.lng)+"/"+data[3])
    if petition.status_code == 200:
        print(petition.text)
        
def main():
    tempHum = threading.Thread(target=DHT,args=(Adafruit_DHT.DHT22,21,))
    rain= threading.Thread(target=Water,args=(20,))
    temp= threading.Thread(target=Temperature,args=(2,))
    tempHum.start()
    rain.start()
    temp.start()
    if __name__:"main"

