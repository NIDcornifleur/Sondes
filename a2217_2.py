# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola.

import sys

import Adafruit_DHT
from time import sleep

sensor_args = { '11': Adafruit_DHT.DHT11,
            '22': Adafruit_DHT.DHT22,
            '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
   sensor = sensor_args[sys.argv[1]]
   pin = sys.argv[2]
else:
   print 'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#'
   print 'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4'
   sys.exit(1)

while True:

  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

  if humidity is not None and temperature is not None:
     print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
  else:
     print 'Failed to get reading. Try again!'
  sleep(60)
