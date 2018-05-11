import time
import numpy as np
import mpc3208 as adc
import data as d

class sampler:
  def __init__(self):
    self.timestamp = time.time()
    self.samples = np.asarray([d.getsensordata()])
  def samplingmatrix(self,sampletime):
    if self.timestamp + sampletime < time.time():
      self.timestamp = time.time() 
      newsample = np.asarray([d.getsensordata()])
      self.samples = np.concatenate((self.samples,newsample))
  def getsamplingmatrix(self):
    return self.samples
  def calcmean(self):
    self.mean = self.samples.mean(axis=0)
    #self.samples = np.asarray([d.getsensordata()])
    return self.mean
  def calcmedian(self):
    self.median = np.median(self.samples,axis=0)
    #self.samples = np.asarray([d.getsensordata()])
    return self.median
  def reset(self):
    self.samples = np.asarray([d.getsensordata()])

