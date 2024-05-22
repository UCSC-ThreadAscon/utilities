"""
  Given a CSV file generated from a PPK2 file, this file
  will return the average energy consumption in both
  mA and mAh.

  For this file to work, the minimum that needs to be save
  from the exported PPK2 CSV are the "timestamp" AND "Current(uA)"
  fields.
"""
import sys
import csv
from common import *

MA_WAKEUP_MINIMUM = 2
UA_WAKEUP_MINIMUM = MA_WAKEUP_MINIMUM * 1000

TRIGGER_MODE = True

def getMicroAmpsList(filename):
  microAmpsList = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      microAmpCurrent = float(row['Current(uA)'])

      if TRIGGER_MODE:
        if microAmpCurrent >= UA_WAKEUP_MINIMUM:
          microAmpsList.append(microAmpCurrent)
      else:
        microAmpsList.append(microAmpCurrent)

      if len(microAmpsList) >= sys.maxsize:
        raise OverflowError("The list is too big.")

  return microAmpsList

def getAverageMicroAmps(microAmpsList):
  length = len(microAmpsList)

  listSum = 0
  for mA in microAmpsList:
    listSum += mA
    if (listSum == sys.float_info.max):
      raise OverflowError("Reach maxed float. Can't add anymore.")

  average = listSum / length
  return average

def getMilliAmps(microAmps):
  return microAmps * 0.001

def getAvgMa(filename):
  microAmpsList = getMicroAmpsList(filename)
  averageMicroAmps = getAverageMicroAmps(microAmpsList)
  # print(f"The average micro amps is {averageMicroAmps}")
  return getMilliAmps(averageMicroAmps)

def getMah(mA, hours):
  return mA * hours

def getAvgMahFile(filename):
  return getMah(getAvgMa(filename), EXPERIMENT_RUNTIME_HOURS)

def getAvgMah(mA):
  return getMah(mA, EXPERIMENT_RUNTIME_HOURS)

def printAvgMa(location, cipher, txPower):
  mA = getAvgMa(files[location][cipher][txPower])
  print(f"The average mA for {location} {cipher} @ {txPower} is {mA} mA")
  return

if __name__ == '__main__':
  printAvgMa("front-door", "aes", "0dbm")
  printAvgMa("front-door", "aes", "9dbm")
  printAvgMa("front-door", "aes", "20dbm")

  printAvgMa("front-door", "ascon128a", "0dbm")
  printAvgMa("front-door", "ascon128a", "9dbm")
  # printAvgMa("front-door", "ascon128a", "20dbm")

  printAvgMa("front-door", "ascon128", "0dbm")
  printAvgMa("front-door", "ascon128", "9dbm")
  printAvgMa("front-door", "ascon128", "20dbm")

  printAvgMa("front-door", "noencrypt", "0dbm")
  printAvgMa("front-door", "noencrypt", "9dbm")
  printAvgMa("front-door", "noencrypt", "20dbm")