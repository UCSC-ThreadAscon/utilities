import csv

"""
  This function is based on the code from the Python Documentation:
  https://docs.python.org/3/library/csv.html#csv.DictReader

  This Stack Overflow post helped me fix a bug I had:
  https://stackoverflow.com/a/38523398
"""
def payloadSizeList(filename):
  with open(filename) as file:
    reader = csv.DictReader(csv)
    for row in reader:
      print(row['Length'])
  return

payloadSizeList('packets_decrypted.csv')