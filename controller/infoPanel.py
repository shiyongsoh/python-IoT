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

        dir = "./uploads/"
        menu = os.listdir(dir)
        # dir = sys.path.append('../modules')
        from modules.FileManager import FileManager
        stats = FileManager(dir+menu[0])
        reading = stats.read()
        
        for temp, humid in reading:
            temperature.append(temp)
            humidity.append(humid)
        # print("temperature"+temperature)
        print("temperature")
        print(temperature)
        print("humidity")
        print(humidity)
        #print("--------------------------------- raw below ---------------------------------")
        reading = stats.read()
        return temperature,humidity
        #2. output data
        # print(reading)
        #3. javascript for analytics to reduce raspbian workload
