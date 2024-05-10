import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *

def getAverageMahRatios(cipher):
  num_locations = len(LOCATIONS)
  average_ratios = [0,            # average @ 0dBm
                    0,            # average @ 9dBm
                    0]            # average @ 20dBm

  for location in LOCATIONS:
    location_ratios = getMahRatios(location, cipher)

    for i in range(0, num_locations):
      average_ratios[i] += location_ratios[i]
  
  for i in range(0, num_locations):
    average_ratios[i] /= num_locations

  return average_ratios


def linegraph_average(title):
  ascon128a_ratios = getAverageMahRatios("ascon128a")
  ascon128_ratios = getAverageMahRatios("ascon128")

  all_ratios = ascon128a_ratios + ascon128_ratios
  y_interval = 1
  y_lim = 10
  y_min = -10

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  ascon128a_lines = plt.plot(TX_POWERS, ascon128a_ratios, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascion128_lines = plt.plot(TX_POWERS, ascon128_ratios, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')

  ax.set_yticks(np.arange(y_min, y_lim, y_interval))
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('mAh difference between AES-CCM (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'average-energy-ratio-sed.pgf'))

if __name__ == "__main__":
  linegraph_average("All Sleepy End Devices")
  plt.show()