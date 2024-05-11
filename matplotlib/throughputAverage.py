import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *

def throughput_averages(title):
  aes = getAvgThroughputs('aes')
  ascon128 = getAvgThroughputs('ascon128')
  ascon128a = getAvgThroughputs('ascon128a')

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
                      label='AES-CCM')
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

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'average-throughput.pgf'))

if __name__ == "__main__":
  throughput_averages("All Full Thread Devices")
  plt.show()
  pass