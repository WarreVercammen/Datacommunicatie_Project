#Invoegen bibliotheken
import time
import board
import busio
import adafruit_si7021
from digitalio import DigitalInOut, Direction

#Objecten aanmaken
uart = busio.UART(board.TX, board.RX, baudrate=115200)
sensor = adafruit_si7021.SI7021(board.I2C())

while True:
    debug = True #Debug-functies activeren
    
    #Sensor uitlezen
    temp  = str(sensor.temperature) + "'C"
    vocht = str(sensor.relative_humidity) + "%"
    
    #Doorsturen data
    uart.write(bytearray("Temperatuur: " + temp))
    uart.write(bytearray("\n"))
    
    time.sleep(0.5)

    uart.write(bytearray("Vochtigheid: " + vocht))
    uart.write(bytearray("\n"))

    time.sleep(0.5)
    

    if(debug):
      print(temp)
      print(vocht)
      print("-----------")
    
    

    

