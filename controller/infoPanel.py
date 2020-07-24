import sys
import os
import json
# uploads = os.
#1. read from csv
class infoPanel:
    def info():
        #defining the variables
        temperature = []
        humidity = []
        time = []
        dir = "./uploads/"
        menu = os.listdir(dir)
        # dir = sys.path.append('../modules')
        from modules.FileManager import FileManager
        stats = FileManager(dir+menu[0])
        reading = stats.read()
        print(reading)
        
        for temp, humid, timing in reading:
            temperature.append(temp)
            humidity.append(humid)
            time.append(timing)
        # print("temperature"+temperature)
        print("temperature")
        print(temperature)
        print("humidity")
        print(humidity)
        print("time")
        print(time)
        #print("--------------------------------- raw below ---------------------------------")
        reading = stats.read()
        return temperature,humidity,time
        #2. output data
        # print(reading)
        #3. javascript for analytics to reduce raspbian workload
