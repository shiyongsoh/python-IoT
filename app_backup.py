from flask import Flask
from flask import render_template

#set up for monitoring potentiometer
import spidev
my_spi=spidev.SpiDev()
my_spi.open(0,0)

#set up for controlling LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

app=Flask(__name__)

def read_ADC(): #function to read potentiometer
    my_spi.max_speed_hz=1350000
    r=my_spi.xfer2([1,0b10000000,0])
    result=((r[1]&3)<<8)+r[2]
    return result

@app.route('/LED_is_ON')
def show_LED_is_ON():
    pot_val=str(read_ADC()) # read potentiometer value
    GPIO.output(27,1) #turn on the physical LED
    return render_template("LED_is_ON.html",value=pot_val) #pass pot_val to webpage 

@app.route('/LED_is_OFF')
def show_LED_is_OFF():
    pot_val=str(read_ADC()) # read potentiometer value
    GPIO.output(27,0) #turn off the physical LED
    return render_template("LED_is_OFF.html",value=pot_val) #pass pot_val to webpage 

#other "web pages" not shown

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0') #0.0.0.0 => accessible to any device on the network
