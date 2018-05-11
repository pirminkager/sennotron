#!/usr/bin/py
import time
import numpy as np
from datetime import datetime
import mpc3208 as adc
#import fakeadc as adc
import os
import writemodule as write
## Variable Definitions
sampletime = 1
numsensors = 8 #int from 1 to 8
filename = datetime.now().strftime('%Y_%m_%d')

## Function Definitions
def getsensordata(nsensors):
  out = [None] * nsensors
  for i in range(nsensors):
    out[i] = adc.readadc(i)
  return out

##Moved to own Module##
#def writetofile(data):
#  file = open(filename,'a')
#  file.write(str(time.time())+';')
#  for i in range(len(data)):
#    file.write(str(data[i])+';')
#  file.write('\n')
#  file.close()
#  return
##

## Class Definitions
class sampler(object):
  def __init__(self):
    self.timestamp = time.time() #initial timestamp
    self.nsensors = 8
  def setsensors(self,par):
    if par <= 8 and par >= 1:
      self.nsensors = par
  def readdata(self,sampletime):
    if self.timestamp + sampletime < time.time():
      try:
        self.timestamp = time.time()
        newsample = np.asarray([getsensordata(self.nsensors)])
        self.samples = np.concatenate((self.samples,newsample))
      except:
        self.timestamp = time.time()
        self.samples = np.asarray([getsensordata(self.nsensors)])
  def data(self):
    return self.samples
  def mean(self):
    mean = self.samples.mean(axis=0)
    return mean
  def median(self):
    median = np.median(self.samples,axis=0)
    return median
  def delete(self):
    self.samples = np.asarray([None])


## Test Section ##
if __name__ == "__main__":

  data = sampler()
  timestamp = time.time()
  i = 0
  while True:
    data.readdata(0.0001)
    if time.time() > timestamp+sampletime:
      data.median()
      data.mean()
      write.tofile(write.filename(),data.median().astype(np.int32))
      timestamp = time.time()
      i = i+1
      print 'test'+str(i)
      print data.median()
      print data.mean()
      data.delete()
