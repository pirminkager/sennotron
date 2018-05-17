## File Parser Module ##

import os
import numpy as np
import csv

fname = 'recipe.txt'

def readfile(filename):
#  try:
   with open(filename,'r') as f:
    for line in f:
      line=line.replace('\t','')
      line=line.replace(' ','')
      if line[0] == '#':
        continue
      for row in csv.reader([line],delimiter=';'):
        try:
	  if 'output' not in locals():
	    output = np.asarray([row])
          else:
            newline = np.asarray([row])
            output = np.concatenate((output,newline))
        except:
          raise
    return output
#  except:
#    print 'Error'

if __name__ == '__main__':
  print readfile(fname)
