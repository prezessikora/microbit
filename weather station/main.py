import bme280
from microbit import *

bme = bme280.bme280()

def changeMeasurement(l):
    display.show(l)
    sleep(400)


def showTemperature():
    changeMeasurement('T')
    display.scroll(int(bme.temperature()))

def showHumidity():
    changeMeasurement('W')
    display.scroll(int(bme.humidity()))

def showPressure():
    changeMeasurement('C')
    display.scroll(int(bme.pressure()))

while True:
    showTemperature()
    showHumidity()
    showPressure()