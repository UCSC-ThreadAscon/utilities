import matplotlib.pyplot as plt
import numpy as np

from energy import *
from common import *

def maBargraph(location, title, finalData):
  energyUsageMa = {
    'No Encryption': (finalData[location]["noencrypt"]["0dbm"],
                      finalData[location]["noencrypt"]["9dbm"],
                      finalData[location]["noencrypt"]["20dbm"]),
    'AES-CCM': (finalData[location]["aes"]["0dbm"],
                finalData[location]["aes"]["9dbm"],
                finalData[location]["aes"]["20dbm"]),
    'ASCON-128a': (finalData[location]["ascon128a"]["0dbm"],
                   finalData[location]["ascon128a"]["9dbm"],
                   finalData[location]["ascon128a"]["20dbm"]),
    'ASCON-128': (finalData[location]["ascon128"]["0dbm"],
                  finalData[location]["ascon128"]["9dbm"],
                  finalData[location]["ascon128"]["20dbm"])
  }

  x = np.arange(len(TX_POWERS))
  width = 0.2
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for attribute, measurement in energyUsageMa.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute,
                  color=cipherToColor[attribute])
    ax.bar_label(rects, padding=3)
    multiplier += 1

  ax.set_ylabel('Average Energy Usage on Wakeup (mA)')
  ax.set_title(title)

  x_width_offset = 0.30
  ax.set_xticks(x + x_width_offset, TX_POWERS_LABELS.values())

  # These y values are set up the bar graph so
  # that the average mA are all shown in the screen.

  # When calculating mAh, the the min and max of the y
  # axis will he hard coded.
  #
  y_values = []
  for cipher in CIPHERS:
    for tx in TX_POWERS:
      y_values.append(finalData[location][cipher][tx])

  y_min = 0
  # y_lim = max(y_values) + 10
  y_lim = 40

  num_ticks = abs(y_lim - y_min) / 10
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [y_lim])

  ax.set_yticks(ticks)
  ax.legend(loc='best', ncols=4)
  ax.set_ylim(y_min, y_lim)

  ax.set_xlabel('TX Power (dBm)')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-bar-graph-mA.pgf'))
  return

if __name__ == "__main__":
  maBargraph("front-door", "Front Door Motion Sensor", finalDataMa)
  # maBargraph("front-door", "Front Door Motion Sensor", finalDataMaNoTrigger)
  plt.show()