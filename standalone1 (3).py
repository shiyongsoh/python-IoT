#done on 14 August 2020 10:01:41am

import RPi.GPIO as GPIO
import dht11
import time
from time import sleep
import datetime
import random
import spidev
import psutil
import requests

from time import sleep
#GUI(Graphics User Interface)
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
#alogrithm for writing to file
from FileManager import FileManager

#computer stats
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs = []
ys = []


#uncomment to do it on actual pi
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=21) #read data using pin 21

GPIO.setup(24,GPIO.OUT) # LED
GPIO.output(24,0)
#computer stats
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs = []
ys = []


#-------------------test code start-----------------------------------#
humidityArray = []
temperatureArray = []
time = 0
timeElapsed = []
numberofRecords = 0


#-------------------test code end-----------------------------------#
#print(f'number of records {numberofRecords}')
#write to file in csv
def likelinessToRain(humidity ,temperature):
    humidity = float(humidity)
    temperature = float(temperature)
    #calculate how likely it is to rain if dewpoint temp is equal to temp
    Td = temperature - ((100-humidity)/5)
    print(Td)
    if Td >= 50:
        print("it is likely to rain")
    if Td <=55:
        print("It looks dry and comfortable now")
    elif Td >=55 and Td <= 65:
        print("Its getting abit humid")
    else:
        print("Time to sweat.....")

def createMenu(dishes, price):
    #menu create
    menuName = "NoMENU"
    count = len(dishes)
    x = 0
    thingsToSend = ''
    #if dishes exist, new inputs will be appended, else, new dishes will be written on the first line of the text
    for x in range(0,len(dishes)):
        print(count)
        if x ==0:
            test = f'{dishes[x]},{price[x]}'
        if x < count-1:
            print("if is running")
            test = f'{dishes[x]},{price[x]}\n'
        else:
            print("else is running")
            test = f'{dishes[x]},{price[x]}'
        thingsToSend += test
    return thingsToSend

def sendToCloud(temp,humi):
    print("send to cloud")
    print(temperatureArray)
    print(humidityArray)
    try:
        resp = requests.get(f"https://api.thingspeak.com/update?api_key=5HVAHWHKOVUQ42U1&field1={temp}&field2={humi}")
        #resp = requests.get(f"https://api.thingspeak.com/update?api_key=5HVAHWHKOVUQ42U1&field1={temp}&field2={humi}")
        print(f'upload temperature at {temp} and humidity at {humi}')
    except requests.exceptions.Timeout:
       print("not able to upload, request timeout")
    except requests.exceptions.TooManyRedirects:
        print("Cannot upload ,Too many redirects")

    except requests.exceptions.RequestException as e:
        print("Cannot upload")
        
class enviroment:
    def tempNhumid(self):
        try:
            while True: #keep reading, unless keyboard is pressed
                result = instance.read()
                if result.is_valid(): #print datetime & sensor values
                    timing = datetime.datetime.now()
                    timing = timing.strftime("%d-%m-%Y_%H:%M:%S")
                    print("Last valid input: " + timing)
                    print("Temperature: %-3.1f C" % result.temperature)
                    print("Humidity: %-3.1f %%" % result.humidity)
                    Temperature = result.temperature
                    Humidity = result.humidity
                    if Temperature >=24:
                        GPIO.output(24,1)
                    else:
                       GPIO.output(24,0)
                    sendToCloud(Temperature,Humidity)
                    likelinessToRain(Humidity,Temperature)
                    csvGen = FileManager('csvGen.csv',f"{Temperature},{Humidity},{timing}\n")
                    csvGen.logged()
                sleep(15) #Thingspeak only data resolution of 15 seconds, so we are going to wait for 15 seconds
                # uploading sensors data
                
        except KeyboardInterrupt:
            print("Cleanup")
            GPIO.cleanup() #Google what this means…
            #return Temperature,Humidity'
            return
    
    def getMositure():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.IN)
        if GPIO.input(4):
            toggle_LED(0)
            return 1
        else:
            toggle_LED(1)
            return 0



def liveSensor():
    plt.plot(timeElapsed,temperatureArray,label = 'temperature and humditity')
    plt.xlabel('temp')
    plt.ylabel('timeElapsed')
    plt.title('Weather station')
    plt.legend("Weather station")
    plt.show()
def HistoryGraph():
    readRecord = FileManager('csvGen.csv')
    hmm = readRecord.read()
    print(hmm)
    plt.ion()
    plt.plot(time,hmm[0],label = 'humditity')
    plt.plot(time,hmm[1],label = 'temperature')
    plt.xlabel('temp')
    plt.ylabel('timeElapsed')
    plt.title('Weather station')
    plt.legend("Weather station")
    plt.show()
def initSensorAndGraph():
    ani = animation.FuncAnimation(fig, sensors, interval=10)
    plt.show()
def sensors(i=None):
    env = enviroment()
    temp,humid = env.tempNhumid()
    
    print(temp)
def getComputerStatus(i):
    if len(xs) >= 10:
        del xs[0]
    if len(ys) >= 10:
        del ys[0]
    print("com stats running")
    cpuUsage = psutil.cpu_percent() #cpu usage
    cpuCoreCount = psutil.cpu_count() #cpu core count
    cpuStats = psutil.cpu_stats() #cpu stats
    cpuTemps = psutil.sensors_temperatures()
    localTime = time.time()
    xs.append(i)
    ys.append(cpuUsage)
    ax1.clear()
    ax1.plot(xs, ys)
    print(f"{cpuTemps},{i}")
    print(ys)
def computerStats():
    if plt.fignum_exists(0):
        print("Is running")
        plt.close(fig)
        ani.close

    else:
        print("Is not running")
    print("computerstats running")
    ani = animation.FuncAnimation(fig, getComputerStatus, interval=1000)
    plt.show()
def showGUI():
    top=Tk()
    simulateLiveSensor = Button(top,text="Live Sensor Graph", command=sensors).pack(side = TOP, pady = 10)
    
    seeHistory = Button(top,text="History Sensor Graph", command=HistoryGraph).pack(side = RIGHT, pady = 10,expand = 20)

    seeComputerStatus = Button(top,text="Computer Sensor Graph", command=computerStats).pack(side = LEFT, pady = 10)
    top.mainloop()
    
    

def init():
    showGUI()

init()
