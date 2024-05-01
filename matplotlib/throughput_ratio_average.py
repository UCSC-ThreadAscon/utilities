import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *
from throughput_ratio import *

def get_average_throughput_ratios(cipher):
  average_throughput_ratios = [0, 0, 0]

  for location in LOCATIONS:
    throughput_ratios = get_throughput_ratios(location, cipher)
  
    for i in range(0, 3):
      average_throughput_ratios[i] += throughput_ratios[i]
  
  for i in range(0, 3):
    average_throughput_ratios[i] /= 3

  return average_throughput_ratios

def throughput_average_ratios(title):
  ascon128 = get_average_throughput_ratios('ascon128')
  ascon128a = get_average_throughput_ratios('ascon128a')

  all_ratios = ascon128 + ascon128a
  y_interval = 5
  y_lim = 20
  y_min = -10

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  ascon128a_lines = plt.plot(TX_POWERS, ascon128a, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascion128_lines = plt.plot(TX_POWERS, ascon128, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')

  ax.set_yticks(np.arange(y_min, y_lim, y_interval))
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('Throughput difference between AES (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-ratio-throughput.pgf'))


if __name__ == "__main__":
  throughput_average_ratios("All Full Thread Devices")
  plt.show()