import csv

"""
  This function is based on the code from the Python Documentation:
  https://docs.python.org/3/library/csv.html#csv.DictReader

  This Stack Overflow post helped me fix a bug I had:
  https://stackoverflow.com/a/38523398
"""
def payloadSizeList(filename):
  lengths = []

  with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
      lengths.append(row['Length'])

  return lengths

decrypted = payloadSizeList('packets_decrypted.csv')
encrypted = payloadSizeList('packets_encrypted.csv')

for i in range(0, min(len(decrypted), len(encrypted))):
  csvRow = i + 2
  difference = abs(int(decrypted[i]) - int(encrypted[i]))
  print(f"Row {csvRow} in CSV: Difference between length {decrypted[i]} and {encrypted[i]} is {difference}")