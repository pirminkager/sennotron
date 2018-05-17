import time
import os
from datetime import datetime

#filename = datetime.now().strftime('%Y_%m_%d')

def date():
  return datetime.now().strftime('%Y_%m_%d')

def tofile(filename,data):
  file = open(filename,'a')
  file.write(str(int(time.time()))+';')
  for i in range(len(data)):
    file.write(str(data[i])+';')
  file.write('\n')
  file.close()
