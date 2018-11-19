import math
import os
import random
import re
import sys
import numpy as np

def diagonalDifference(ar):
  ar = np.array(ar).reshape(3,3)
  
  #Calculate first diagonal
  first = ar.trace()
  
  #Calculate second diagonal
  second = np.flip(ar, 0).trace()
  
  difference = abs[first - second]
  
  return difference 
