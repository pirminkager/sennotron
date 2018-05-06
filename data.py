#!/usr/bin/py
import time
#import mpc3208
import fakeadc as adc
import os
## Variable Definitions
sampletime = 0.5
numsensors = 7 #int from 0 to 7
filename = 'test'

## Function Definitions
def getsensordata():
  out = [None] * numsensors
  for i in range(numsensors):
    out[i] = adc.readadc(i)
  return out

def writetofile(data):
  file = open(filename,'a')
  file.write(str(time.time())+';')
  for i in range(len(data)):
    file.write(str(data[i])+';')
  file.write('\n')
  file.close()
  return

if __name__ == "__main__":
  ## Test Outputs ##
  timestamp = time.time()
  i = 0
  while True:
    if time.time() > timestamp+sampletime:
      writetofile(getsensordata())
      timestamp = time.time()
      i = i+1
      print 'test'+str(i)
