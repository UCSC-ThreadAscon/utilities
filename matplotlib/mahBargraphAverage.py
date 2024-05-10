import matplotlib.pyplot as plt
import numpy as np

from energy import *
from common import *
from average import *

def mahBargraphAverage(title):
  mean_energy_usage = {
    'AES-CCM': (getAvgMahAll("aes", "0dbm"),
                getAvgMahAll("aes", "9dbm"),
                getAvgMahAll("aes", "20dbm")),
    'ASCON-128a': (getAvgMahAll("ascon128a", "0dbm"),
                   getAvgMahAll("ascon128a", "9dbm"),
                   getAvgMahAll("ascon128a", "20dbm")),
    'ASCON-128': (getAvgMahAll("ascon128", "0dbm"),
                  getAvgMahAll("ascon128", "9dbm"),
                  getAvgMahAll("ascon128", "20dbm")),
  }

  x = np.arange(len(TX_POWERS))
  width = 0.25
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for attribute, measurement in mean_energy_usage.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute,
                  color=cipherToColor[attribute])
    # ax.bar_label(rects, padding=4)
    multiplier += 1

  ax.set_ylabel('Average (mAh)')
  ax.set_title(title)
  ax.set_xticks(x + width, TX_POWERS)

  y_min = 0
  y_lim = 10

  num_ticks = abs(y_lim - y_min) / 10
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [10])

  ax.set_yticks(ticks)
  ax.legend(loc='best', ncols=3, fontsize=8)
  ax.set_ylim(y_min, y_lim)

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'average-energy-bar-graph.pgf'))
  return

if __name__ == "__main__":
  mahBargraphAverage("All Sleepy End Devices")
  plt.show()