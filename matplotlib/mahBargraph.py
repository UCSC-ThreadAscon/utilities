import matplotlib.pyplot as plt
import numpy as np

from energy import *
from common import *

def mahBargraph(location, title):
  energyUsageMah = {
    'AES-CCM': (getAvgMah(prelimData[location]["aes"]["0dbm"]),
                getAvgMah(prelimData[location]["aes"]["9dbm"]),
                getAvgMah(prelimData[location]["aes"]["20dbm"])),
    'ASCON-128a': (getAvgMah(prelimData[location]["ascon128a"]["0dbm"]),
                    getAvgMah(prelimData[location]["ascon128a"]["9dbm"]),
                    getAvgMah(prelimData[location]["ascon128a"]["20dbm"])),
    'ASCON-128': (getAvgMah(prelimData[location]["ascon128"]["0dbm"]),
                  getAvgMah(prelimData[location]["ascon128"]["9dbm"]),
                  getAvgMah(prelimData[location]["ascon128"]["20dbm"])),
  }

  x = np.arange(len(TX_POWERS))
  width = 0.25
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for attribute, measurement in energyUsageMah.items():
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

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-bar-graph.pgf'))
  return

if __name__ == "__main__":
  mahBargraph("front-door", "Front Door Motion Sensor")
  plt.show()