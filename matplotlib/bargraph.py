import matplotlib.pyplot as plt
import numpy as np

txpower = ("20 dBm", "0dBm", "-9 dBm")
mean_energy_usage = {
    'AES-CCM': (18.35, 18.43, 14.98),
    'ASCON-128a': (38.79, 48.83, 47.50),
    'ASCON-128': (189.95, 195.82, 217.19),
}

x = np.arange(len(txpower))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in mean_energy_usage.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Energy Consumption (mA)')
ax.set_title('Front Door ESP32-H2')
ax.set_xticks(x + width, txpower)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

plt.show()