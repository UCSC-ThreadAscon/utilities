"""
  Given a CSV file generated from a PPK2 file, this file
  will return the average energy consumption in both
  mA and mAh.

  For this file to work, the minimum that needs to be save
  from the exported PPK2 CSV are the "timestamp" AND "Current(uA)"
  fields.
"""
import csv
from common import *

def getMicroAmpsList(filename):
  microAmpsList = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      microAmpCurrent = float(row['Current(uA)'])
      microAmpsList.append(microAmpCurrent)

  return microAmpsList

def getAverageMicroAmps(microAmpsList):
  length = len(microAmpsList)
  listSum = sum(microAmpsList)
  average = listSum / length
  return average

def getMilliAmps(microAmps):
  # According to Google `1 micro amp` === `0.001 milli amps`
  return microAmps * 0.001

def getAvgMa(filename):
  microAmpsList = getMicroAmpsList(filename)
  averageMicroAmps = getAverageMicroAmps(microAmpsList)
  return getMilliAmps(averageMicroAmps)

def getMAh(mA, hours):
  return mA * hours

def getAvgMAh(filename):
  return getMAh(getAvgMa(filename), EXPERIMENT_RUNTIME_HOURS)


if __name__ == '__main__':
  filename = 'aes-0dbm-frontdoor-sample.csv'
  print(getAvgMa(filename))