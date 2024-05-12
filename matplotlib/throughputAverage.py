import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *

def tpAveragesLine(title):
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

def tpAveragesBar(title):
  aes = getAvgThroughputs('aes')
  ascon128 = getAvgThroughputs('ascon128')
  ascon128a = getAvgThroughputs('ascon128a')

  throughputs = {
    'AES-CCM': (aes[0],
                aes[1],
                aes[2]),
    'ASCON-128a': (ascon128a[0],
                   ascon128a[1],
                   ascon128a[2]),
    'ASCON-128': (ascon128[0],
                  ascon128[1],
                  ascon128[2]),
  }

  x = np.arange(len(TX_POWERS))
  width = 0.25 
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  for attribute, measurement in throughputs.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute,
                  color=cipherToColor[attribute])
    # ax.bar_label(rects, padding=4)
    multiplier += 1

  ax.set_ylabel('Throughput (bytes/second)')
  ax.set_title(title)
  ax.set_xticks(x + width, TX_POWERS)

  y_interval = 50
  y_lim = 1200
  y_min = 0

  ticks = np.arange(y_min, y_lim, y_interval)
  ticks = np.append(ticks, [y_lim])

  ax.set_yticks(ticks)
  ax.legend(loc='best', ncols=3)
  ax.set_ylim(y_min, y_lim)

  plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'throughput-average-bar-graph.pgf'))
  return

if __name__ == "__main__":
  # tpAveragesLine("All Full Thread Devices")
  tpAveragesBar("All Full Thread Devices")
  plt.show()
  pass