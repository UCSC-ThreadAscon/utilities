import matplotlib.pyplot as plt
import numpy as np

from average import *
from common import *

def bargraph(location, title):
  mean_energy_usage = {
    'AES-CCM': (prelimData[location]["aes"]["0dbm"],
                prelimData[location]["aes"]["9dbm"],
                prelimData[location]["aes"]["20dbm"]),
    'ASCON-128a': (prelimData[location]["ascon128a"]["0dbm"],
                   prelimData[location]["ascon128a"]["9dbm"],
                   prelimData[location]["ascon128a"]["20dbm"]),
    'ASCON-128': (prelimData[location]["ascon128"]["0dbm"],
                  prelimData[location]["ascon128"]["9dbm"],
                  prelimData[location]["ascon128"]["20dbm"]),
  }

  # the label locations
  x = np.arange(len(TX_POWERS))

  # the width of the bars
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

  ax.set_ylabel('Average (mA)')
  ax.set_title(title)
  ax.set_xticks(x + width, TX_POWERS)

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
  bargraph("front-door", "Front Door Motion Sensor")
  bargraph("air-quality", "Air Quality Monitor")
  bargraph("second-story", "Second StoryMotion Sensor")
  plt.show()