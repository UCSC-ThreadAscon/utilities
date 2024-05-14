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

def getMicroAmpsList(filename):
  microAmpsList = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      microAmpCurrent = float(row['Current(uA)'])
      microAmpsList.append(microAmpCurrent)

      if len(microAmpsList) > sys.maxsize:
        raise OverflowError("The list is too big.")

  return microAmpsList

def getAverageMicroAmps(microAmpsList):
  length = len(microAmpsList)
  listSum = sum(microAmpsList)

  listSum = 0
  for mA in microAmpsList:
    listSum += mA
    if (listSum == sys.float_info.max):
      raise OverflowError("Reach maxed float. Can't add anymore")

  average = listSum / length
  return average

def getMilliAmps(microAmps):
  return microAmps * 0.001

def getAvgMa(filename):
  microAmpsList = getMicroAmpsList(filename)
  averageMicroAmps = getAverageMicroAmps(microAmpsList)
  return getMilliAmps(averageMicroAmps)

def getMah(mA, hours):
  return mA * hours

def getAvgMahFile(filename):
  return getMah(getAvgMa(filename), EXPERIMENT_RUNTIME_HOURS)

def getAvgMah(mA):
  return getMah(mA, EXPERIMENT_RUNTIME_HOURS)

def printAvgMa(location, cipher):
  mA = getAvgMa(files[location][cipher]["0dbm"])
  print(f"The average mA for {location} {cipher} @ 0dBm is {mA} mA")

  mA = getAvgMa(files[location][cipher]["9dbm"])
  print(f"The average mA for {location} {cipher} @ 9dBm is {mA} mA")

  mA = getAvgMa(files[location][cipher]["20dbm"])
  print(f"The average mA for {location} {cipher} @ 20dBm is {mA} mA")

  return

if __name__ == '__main__':
  printAvgMa("washing-machine", "ascon128a")
  printAvgMa("washing-machine", "ascon128")
  printAvgMa("washing-machine", "aes")

  printAvgMa("second-story", "ascon128a")
  printAvgMa("second-story", "ascon128")
  printAvgMa("second-story", "aes")

  printAvgMa("front-door", "aes")
  printAvgMa("front-door", "ascon128a")
  printAvgMa("front-door", "ascon128")