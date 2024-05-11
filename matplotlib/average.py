from common import *
from energy import *

def getAvgMahAll(cipher, tx_power):
  sum = 0
  for location in LOCATIONS_ENERGY:
    sum += getAvgMah(prelimData[location][cipher][tx_power])
  return sum / len(LOCATIONS_ENERGY)

"""
  EQUATION TO CALCULATE RATIO
  ---------------------------
  mAh_aes => mAh of AES cipher for a given location
  mAh_ascon => mAh of ASCON-128/a for a given location

  [ 1 - (mAh_ascon / mAh_aes) ]    *    100
        |-------------------|
          % mAh_ascon is made
        up relative to mAh_aes

  |---------------------------|
    % gap between mAh_ascon and
    mAh_aes

  For the value shown above:
    if > 0%, then it shows that mAh_ascon is % SMALLER than AES.
    if < 0%, then it shows that mAH_ascon is % BIGGER than AES.
  
  However, we want to show mAh_ascon being smaller as a decrease,
  and mAh_ascon being bigger as an increase.

  So, when we multiply by -1, we get:
    if > 0%, then it shows that mAh_ascon is % BIGGER than AES.
    if < 0%, then it shows that mAH_ascon is % AES than AES.

  The format of the ratios array:
  
    [   ratio @ 0 dBm,  ratio @ 9 dBm,  ratio @ 20dBm   ]
"""
def getMahRatios(location, cipher):
  ratios = []
  for tx in TX_POWERS:
    value_cipher = getAvgMah(prelimData[location][cipher][tx])
    value_aes = getAvgMah(prelimData[location]["aes"][tx])

    ratio = 1 - (value_cipher / value_aes)
    ratio *= 100
    ratio *= -1

    ratios.append(ratio)
  return ratios

"""
  x bytes        ? bytes
  -------  ===  ---------
   y ms          1 ms  

  x / y              bytes / ms  
  (x / y) * 1000     bytes / second

The array will end up being:

    [throughput @ 0dBm, throughput @ 9dBm, throughput @ 20dBm]
"""
def getThroughputs(location, cipher):
  throughputs = []
  for tx in TX_POWERS:
    throughput = \
      (averageRTTs[location][cipher][tx] / THROUGHPUT_EXP_PACKET_SIZE) * 1000
    throughputs.append(throughput)
  return throughputs

def getAvgThroughputs(cipher):
  avgThroughputs = [0,        # 0 dBm
                    0,        # 9 dBm
                    0]        # 20 dBm
  numLocations = len(LOCATIONS_THROUGHPUT)

  for location in LOCATIONS_THROUGHPUT:
    location_throughputs = getThroughputs(location, cipher)
    for i in range(0, numLocations):
      avgThroughputs[i] += location_throughputs[i]
  
  for i in range(0, numLocations):
    avgThroughputs[i] /= numLocations

  return avgThroughputs

def getThroughputRatios(location, cipher):
  ratios = []
  for tx in TX_POWERS:
    throughput_cipher = averageRTTs[location][cipher][tx]
    throughput_aes = averageRTTs[location]["aes"][tx]

    ratio = 1 - (throughput_cipher / throughput_aes)
    ratio *= 100
    ratio *= -1
    ratios.append(ratio)

  return ratios

def getAvgThroughputRatios(cipher):
  avgThroughputRatios = [0, 0, 0]
  numLocations = len(LOCATIONS_THROUGHPUT)

  for location in LOCATIONS_THROUGHPUT:
    throughput_ratios = getThroughputRatios(location, cipher)
  
    for i in range(0, numLocations):
      avgThroughputRatios[i] += throughput_ratios[i]
  
  for i in range(0, numLocations):
    avgThroughputRatios[i] /= numLocations

  return avgThroughputRatios