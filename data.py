#!/usr/bin/py
import time
import numpy as np
from datetime import datetime
import mpc3208 as adc
#import fakeadc as adc
import os
## Variable Definitions
sampletime = 1
numsensors = 8 #int from 1 to 8
filename = datetime.now().strftime('%Y_%m_%d')

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

## Class Definitions

class datasampler:
  def __init__(self):
    self.timestamp = time.time()
    self.samples = np.asarray([getsensordata()])
  def samplingmatrix(self,sampletime):
    if self.timestamp + sampletime < time.time():
      self.timestamp = time.time()
      newsample = np.asarray([getsensordata()])
      self.samples = np.concatenate((self.samples,newsample))
  def getsamplingmatrix(self):
    return self.samples
  def calcmean(self):
    self.mean = self.samples.mean(axis=0)
    #self.samples = np.asarray([getsensordata()])
    return self.mean
  def calcmedian(self):
    self.median = np.median(self.samples,axis=0)
    #self.samples = np.asarray([getsensordata()])
    return self.median
  def reset(self):
    self.samples = np.asarray([getsensordata()])


## Test Section ##
if __name__ == "__main__":

  data = datasampler()
  timestamp = time.time()
  i = 0
  while True:
    data.samplingmatrix(0.0001)
    if time.time() > timestamp+sampletime:
      data.calcmedian()
      data.reset()
      writetofile(data.median.astype(np.int32))
      timestamp = time.time()
      i = i+1
      print 'test'+str(i)
      print data.median
