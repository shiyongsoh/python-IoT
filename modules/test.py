from FileManager import FileManager
import os 
import random
import datetime
def createMenu(dishes, price, timing):
    #menu create
    menuName = "NoMENU"
    count = len(dishes)
    x = 0
    thingsToSend = ''
    #if dishes exist, new inputs will be appended, else, new dishes will be written on the first line of the text
    for x in range(0,len(dishes)):
        print(count)
        if x ==0:
            test = f'{dishes[x]},{price[x]},{timing[x]}'
        if x < count-1:
            print("if is running")
            test = f'{dishes[x]},{price[x]},{timing[x]}\n'
        else:
            print("else is running")
            test = f'{dishes[x]},{price[x]},{timing[x]}'
        thingsToSend += test
    return thingsToSend

print("success")
for i in range(5):
    Temperature =random.randint(30,35)
    Humidity =random.randint(30,35)
    timing = datetime.datetime.now()
    timing = timing.strftime("%d-%m-%Y_%H:%M:%S")
    print(timing)
    # Temperature = createMenu(Temperature,Humidity,timing)
    csvGen = FileManager('csvGen.csv',f"{Temperature},{Humidity},{timing}\n")
    csvGen.logged()


# print(os.listdir(os.getcwd()))
