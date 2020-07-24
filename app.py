from flask import Flask
from flask import render_template
import json
from time import ctime

app=Flask(__name__)

# from sensors import enviroment # uncomment this in raspberry pi

@app.route('/')
def index():
    from controller.infoPanel import infoPanel as displays
    # sensors.getMoisture()
    temp, humid, time  = displays.info()
    # print(hmm)
    # hmm = str(hmm)
    temperature = json.dumps({"temperature":temp})
    humidity = json.dumps({"humidity":humid})
    print(temperature)
    print(humidity)
    dataToSend = temperature, humidity, time
    dataToSend = json.dumps({"dataToSend":dataToSend})
    return render_template("index.html",temperature = temp,humidity = humid,dataToSend =dataToSend, time=time,ctime = ctime())

@app.route('/stats')
def stats():
    from controller.statsPanel import statsPanel as stats
    cpuUsage,cpuCoreCount,cpuStats,RAM,cpuTemps,cpuFans,battery = stats.Computer()
    print(cpuUsage)
    return render_template("stats.html",cpuUsage=cpuUsage,cpuCoreCount=cpuCoreCount,cpuStats=cpuStats,RAM=RAM,cpuTemps=cpuTemps,cpuFans=cpuFans,battery=battery)

@app.route('/test')
def test():
    return render_template("info.html",test="asdf")



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0') #0.0.0.0 => accessible to any device on the network

