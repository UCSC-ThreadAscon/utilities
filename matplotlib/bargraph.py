import matplotlib.pyplot as plt
import numpy as np

from average import *
from common import *

txpower = ("-9 dBm", "0dBm", "20 dBm")
mean_energy_usage = {
  'AES-CCM': (getAvgMAh(files["front-door"]["aes"]["-9dbm"]),
              getAvgMAh(files["front-door"]["aes"]["0dbm"]),
              getAvgMAh(files["front-door"]["aes"]["20dbm"])),
  'ASCON-128a': (getAvgMAh(files["front-door"]["ascon128a"]["-9dbm"]),
                  getAvgMAh(files["front-door"]["ascon128a"]["0dbm"]),
                  getAvgMAh(files["front-door"]["ascon128a"]["20dbm"])),
  'ASCON-128': (0,
                getAvgMAh(files["front-door"]["ascon128"]["0dbm"]),
                getAvgMAh(files["front-door"]["ascon128"]["20dbm"])),
}

x = np.arange(len(txpower))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 3)
fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

for attribute, measurement in mean_energy_usage.items():
  offset = width * multiplier
  rects = ax.bar(x + offset, measurement, width, label=attribute,
                 color=cipherToColor[attribute])
  ax.bar_label(rects, padding=4)
  multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Energy Consumption (mAh)')
ax.set_title('Front Door ESP32-H2')
ax.set_xticks(x + width, txpower)

y_lim = 10
ax.set_yticks(np.arange(0, y_lim, 0.5))
ax.legend(loc='upper right', ncols=3)
ax.set_ylim(0, y_lim)

plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'bargraph.pgf'))
# plt.show()