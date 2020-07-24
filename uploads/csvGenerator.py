
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

from FileManager import FileManager
Temperature=[23,24,25,23,21,22,24,26,27,26]
Humidity=[55,57,60,59,62,66,70,68,66,65]
Temperature = createMenu(Temperature,Humidity)
csvGen = FileManager('csvGen.csv',Temperature)
csvGen.writing()