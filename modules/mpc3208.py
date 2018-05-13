#!/usr/bin/python

import spidev
import time

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=80000

# Function to read SPI data from MCP3208 chip
# Channel must be an integer 0-7
def readadc(ch):
  b1 = (0b11000 | ch)<<3
  adc = spi.xfer2([b1,0x00,0x00])
  #time.sleep(0.0000001) #Not sure if sleep is needed. Looks like it works the same
  data = ((adc[0]<<11) + (adc[1]<<3) + (adc[2]>>5)) & 0b0000000111111111111 
  return data

if __name__=="__main__":
  i=0
  while True:
    out = readadc(i)
    print 'ch: {1:1d} read: {0:4d}'.format(out,i)
    i=i+1
    if i>7:
      i=0
