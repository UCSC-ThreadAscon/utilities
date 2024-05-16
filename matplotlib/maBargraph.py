import matplotlib.pyplot as plt
import numpy as np

from energy import *
from common import *

def maBargraph(location, title):
  energyUsageMa = {
    'AES-CCM': (testMaAll[location]["aes"]["0dbm"],
                testMaAll[location]["aes"]["9dbm"],
                testMaAll[location]["aes"]["20dbm"]),
    'ASCON-128a': (testMaAll[location]["ascon128a"]["0dbm"],
                   testMaAll[location]["ascon128a"]["9dbm"],
                   testMaAll[location]["ascon128a"]["20dbm"]),
    'ASCON-128': (testMaAll[location]["ascon128"]["0dbm"],
                  testMaAll[location]["ascon128"]["9dbm"],
                  testMaAll[location]["ascon128"]["20dbm"]),
  }

  x = np.arange(len(TX_POWERS))
  width = 0.25 
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for attribute, measurement in energyUsageMa.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute,
                  color=cipherToColor[attribute])
    ax.bar_label(rects, padding=4)
    multiplier += 1

  ax.set_ylabel('Average (mA)')
  ax.set_title(title)
  ax.set_xticks(x + width, TX_POWERS)

  # These y values are set up the bar graph so
  # that the average mA are all shown in the screen.

  # When calculating mAh, the the min and max of the y
  # axis will he hard coded.
  #
  y_values = []
  for cipher in CIPHERS:
    for tx in TX_POWERS:
      y_values.append(prelimData[location][cipher][tx])

  y_min = 0
  y_lim = max(y_values) + 0.5

  num_ticks = abs(y_lim - y_min) / 10
  ticks = np.arange(0, y_lim, num_ticks)

  ax.set_yticks(ticks)
  ax.legend(loc='best', ncols=3, fontsize=8)
  ax.set_ylim(y_min, y_lim)

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-bar-graph-mA.pgf'))
  return

if __name__ == "__main__":
  maBargraph("front-door", "Front Door Motion Sensor")
  maBargraph("air-quality", "Air Quality Monitor")
  maBargraph("second-story", "Second Story Door Motion Sensor")
  plt.show()