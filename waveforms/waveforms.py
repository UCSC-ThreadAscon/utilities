import sys
import csv
import os

"""
TO-DO: Calculate how long each wakeup lasted.
Change the threshold to slightly above 7.5-8 uA.
"""
UA_WAKEUP_MINIMUM = 10

def getMa(uA):
  return uA * 0.001

def getMah(mA, hours):
  return mA * hours

def getUaList(filename):
  uAList = []
  timestamps = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      uA = float(row['Current(uA)'])
      time = float(row['Timestamp(ms)'])

      if uA >= UA_WAKEUP_MINIMUM:
        uAList.append(uA)
        timestamps.append(time)
  
      if len(uAList) >= sys.maxsize:
        raise OverflowError("The list is too big.")
  
  durationMs = timestamps[-1] - timestamps[0]

  return (uAList, durationMs)

def getAvgUa(listUa):
  length = len(listUa)
  listSum = 0

  for mA in listUa:
    listSum += mA
    if (listSum == sys.float_info.max):
      raise OverflowError("Reach maxed float. Can't add anymore.")

  average = listSum / length
  return average

def getAvgMa(filename):
  mAList, durationMs = getUaList(filename)
  avgUa = getAvgUa(mAList)
  return (getMa(avgUa), durationMs)

if __name__ == '__main__':
  aesWaveformPath = os.path.join('.', 'raw_data', 'AES 20 dBm.csv')
  mA, durationMs = getAvgMa(aesWaveformPath)
  print(f"The average wakeup at AES @ 20 dBm is: {mA} mA.")
  print(f"The average wakeup time at AES @ 20 dBm is: {durationMs} ms.")
  print()

  noEncryptWaveformPath = os.path.join('.', 'raw_data', 'No Encrypt 20 dBm.csv')
  mA, durationMs = getAvgMa(noEncryptWaveformPath)
  print(f"The average wakeup at No Encryption @ 20 dBm is: {mA} mA.")
  print(f"The average wakeup time at No Encryption @ 20 dBm is: {durationMs} ms.")
  print()

  waveformPathAscon128a = os.path.join('.', 'raw_data', 'ASCON-128a 20 dBm.csv')
  mA, durationMs = getAvgMa(waveformPathAscon128a)
  print(f"The average wakeup at ASCON-128a @ 20 dBm is: {mA} mA.")
  print(f"The average wakeup time at ASCON-128a @ 20 dBm is: {durationMs} ms.")
  print()

  waveformPathAscon128 = os.path.join('.', 'raw_data', 'ASCON-128 20 dBm.csv')
  mA, durationMs = getAvgMa(waveformPathAscon128)
  print(f"The average wakeup at ASCON-128 @ 20 dBm is: {mA} mA.")
  print(f"The average wakeup time at ASCON-128 @ 20 dBm is: {durationMs} ms.")
  print()