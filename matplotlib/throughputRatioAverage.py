import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *

def throughput_average_ratios(title):
  ascon128 = getAvgThroughputRatios('ascon128')
  ascon128a = getAvgThroughputRatios('ascon128a')

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
  ax.set_ylabel('Throughput difference between AES-CCM (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'average-ratio-throughput.pgf'))

if __name__ == "__main__":
  throughput_average_ratios("All Full Thread Devices")
  plt.show()