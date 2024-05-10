from common import *
from energy import *

def getAvgMahAll(cipher, tx_power):
  sum = 0
  for location in LOCATIONS:
    sum += getAvgMah(prelimData[location][cipher][tx_power])
  return sum / len(LOCATIONS)