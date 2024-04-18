import matplotlib.pyplot as plt
import numpy as np

from average import *

files = {
    "front-door": {
        "aes": {
            "0dbm": "aes-0dbm-frontdoor-sample.csv",
            "20dbm": "aes-20dbm-frontdoor-sample.csv",
            "-9dbm": "aes-neg9dbm-frontdoor-sample.csv"
        },
        "ascon128a": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        }
    },
    "washing-machine": {
        "aes": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128a": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        }
    },
    "second-story": {
        "aes": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128a": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        }
    }
}

txpower = ("20 dBm", "0dBm", "-9 dBm")
mean_energy_usage = {
    'AES-CCM': (getAvgMa(files["front-door"]["aes"]["20dbm"]),
                getAvgMa(files["front-door"]["aes"]["0dbm"]),
                getAvgMa(files["front-door"]["aes"]["-9dbm"])),
    'ASCON-128a': (0, 0, 0),
    'ASCON-128': (0, 0, 0),
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
ax.set_ylim(0, 4)

plt.show()