import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *
from throughput import *

"""
  x bytes        ? bytes
  -------  ===  -------
   y ms          1 ms  

  x / y              bytes / ms  
  (x / y) * 1000     bytes / second
"""

TX_POWERS = ["0dbm", "9dbm", "20dbm"]

PACKET_SIZE = 50

def get_average_throughputs(cipher):
  average_throughputs = [0, 0, 0]
  for location in LOCATIONS:
    location_throughputs = get_throughputs(location, cipher)

    for i in range(0, 3):
      average_throughputs[i] += location_throughputs[i]
  
  for i in range(0, 3):
    average_throughputs[i] /= 3

  return average_throughputs

def throughput_averages(title):
  aes = get_average_throughputs('aes')
  ascon128 = get_average_throughputs('ascon128')
  ascon128a = get_average_throughputs('ascon128a')

  all_ratios = aes + ascon128 + ascon128a
  # y_interval = 15
  # y_lim = max(all_ratios) + y_interval
  # y_min = min(all_ratios) - y_interval

  y_interval = 50
  y_lim = 1200
  y_min = 800

  ticks = np.arange(y_min, y_lim, y_interval)
  ticks = np.append(ticks, [y_lim])

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  aes_lines = plt.plot(TX_POWERS, aes, 'o--',
                      color=cipherToColor['AES-CCM'],
                      label='AES')
  ascon128a_lines = plt.plot(TX_POWERS, ascon128a, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascion128_lines = plt.plot(TX_POWERS, ascon128, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')

  ax.set_yticks(ticks)
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('Throughput (bytes/second)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-throughput.pgf'))

if __name__ == "__main__":
  throughput_averages("All Full Thread Devices")
  plt.show()
  pass