import matplotlib.pyplot as plt
import numpy as np

from average import *
from common import *

txpower = ("20 dBm", "0dBm", "-9 dBm")
mean_energy_usage = {
    'AES-CCM': (getAvgMa(files["front-door"]["aes"]["20dbm"]),
                getAvgMa(files["front-door"]["aes"]["0dbm"]),
                getAvgMa(files["front-door"]["aes"]["-9dbm"])),
    'ASCON-128a': (getAvgMa(files["front-door"]["ascon128a"]["20dbm"]),
                   getAvgMa(files["front-door"]["ascon128a"]["0dbm"]),
                   getAvgMa(files["front-door"]["ascon128a"]["-9dbm"])),
    'ASCON-128': (getAvgMa(files["front-door"]["ascon128"]["20dbm"]),
                  getAvgMa(files["front-door"]["ascon128"]["0dbm"]),
                  2.22543543),
}

x = np.arange(len(txpower))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in mean_energy_usage.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=4)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Energy Consumption (mA)')
ax.set_title('Front Door ESP32-H2')
ax.set_xticks(x + width, txpower)

y_lim = 3.5
ax.set_yticks(np.arange(0, y_lim, 0.3))
ax.legend(loc='upper right', ncols=3)
ax.set_ylim(0, y_lim)

plt.show()