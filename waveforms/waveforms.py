import sys
import csv
import os

MA_WAKEUP_MINIMUM = 0.5
UA_WAKEUP_MINIMUM = MA_WAKEUP_MINIMUM * 1000

def getMa(uA):
  return uA * 0.001

def getMah(mA, hours):
  return mA * hours

def uAList(filename):
  microAmpsList = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      microAmpCurrent = float(row['Current(uA)'])

      if microAmpCurrent >= UA_WAKEUP_MINIMUM:
        microAmpsList.append(microAmpCurrent)
  
      if len(microAmpsList) >= sys.maxsize:
        raise OverflowError("The list is too big.")

  return microAmpsList

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
  mAList = uAList(filename)
  avgUa = getAvgUa(mAList)
  return getMa(avgUa)

if __name__ == '__main__':
  aesWaveformPath = os.path.join('.', 'raw_data', 'AES 20 dBm.csv')
  print(f"The average wakeup at AES @ 20 dBm is: {getAvgMa(aesWaveformPath)} mA")

  noEncryptWaveformPath = os.path.join('.', 'raw_data', 'No Encrypt 20 dBm.csv')
  print(f"The average wakeup at AES @ 20 dBm is: {getAvgMa(noEncryptWaveformPath)} mA")
  pass