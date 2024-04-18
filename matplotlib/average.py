"""
  Given a CSV file generated from a PPK2 file, this file
  will return the average energy consumption in both
  mA and mAh.
"""
import csv

def getMicroAmpsList(filename):
  microAmpsList = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      microAmpsList.append(row['Current(uA)'])

  return microAmpsList

print(getMicroAmpsList('aes-0dbm-frontdoor-sample.csv'))