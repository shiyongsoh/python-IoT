import RPi.GPIO as GPIO
import dht11
import time
import datetime
from FileManager import FileManager

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=21) #read data using pin 21

#write to file in csv
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


class enviroment:
    def tempNhumid():
        try:
            while True: #keep reading, unless keyboard is pressed
                result = instance.read()
                if result.is_valid(): #print datetime & sensor values
                    print("Last valid input: " +     
                        str(datetime.datetime.now()))
                    print("Temperature: %-3.1f C" % result.temperature)
                    print("Humidity: %-3.1f %%" % result.humidity)
                time.sleep(0.5) #short delay between reads

        except KeyboardInterrupt:
            print("Cleanup")
            GPIO.cleanup() #Google what this means…
