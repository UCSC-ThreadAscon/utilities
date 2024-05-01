import matplotlib.pyplot as plt
import numpy as np

from average import *
from common import *

def bargraph(location, title):
  txpower = ("0 dBm", "9 dBm", "20 dBm")
  mean_energy_usage = {
    'AES-CCM': (getAvgMAh(prelimData[location]["aes"]["0dbm"]),
                getAvgMAh(prelimData[location]["aes"]["9dbm"]),
                getAvgMAh(prelimData[location]["aes"]["20dbm"])),
    'ASCON-128a': (getAvgMAh(prelimData[location]["ascon128a"]["0dbm"]),
                    getAvgMAh(prelimData[location]["ascon128a"]["9dbm"]),
                    getAvgMAh(prelimData[location]["ascon128a"]["20dbm"])),
    'ASCON-128': (getAvgMAh(prelimData[location]["ascon128"]["0dbm"]),
                  getAvgMAh(prelimData[location]["ascon128"]["9dbm"]),
                  getAvgMAh(prelimData[location]["ascon128"]["20dbm"])),
  }

  x = np.arange(len(txpower))  # the label locations
  width = 0.25  # the width of the bars
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

  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Average (mAh)')
  ax.set_title(title)
  ax.set_xticks(x + width, txpower)

  y_values = []
  for cipher in ["aes", "ascon128a", "ascon128"]:
    for tx in ["0dbm", "9dbm", "20dbm"]:
      y_values.append(getAvgMAh(prelimData[location][cipher][tx]))

  y_min = 0
  y_lim = 9

  num_ticks = abs(y_lim - y_min) / 9
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [9])

  ax.set_yticks(ticks)

  ax.legend(loc='best', ncols=3, fontsize=8)
  ax.set_ylim(y_min, y_lim)

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-bar-graph.pgf'))
  return

if __name__ == "__main__":
  bargraph("front-door", "Front Door Sleepy End Device")
  bargraph("washing-machine", "Washing Machine Sleepy End Device")
  bargraph("second-story", "Second Story Sleepy End Device")
  plt.show()