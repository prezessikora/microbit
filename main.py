import tcs3472
from microbit import *

light_sensor = tcs3472.tcs3472()

while True:
    light = light_sensor.light()
    pixels_no = (light/65535)*100
    display.scroll(int(light))