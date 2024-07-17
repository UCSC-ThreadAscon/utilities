import matplotlib.pyplot as plt
import numpy as np

from delay_common import *

SHOW_BAR_LABELS = False

toDisplay = {
  'No Encryption': (avgDelaysUs["no encryption"]["0 dBm"],
                    avgDelaysUs["no encryption"]["9 dBm"],
                    avgDelaysUs["no encryption"]["20 dBm"]),
  'AES-CCM': (avgDelaysUs["aes"]["0 dBm"],
              avgDelaysUs["aes"]["9 dBm"],
              avgDelaysUs["aes"]["20 dBm"]),
  'ASCON-128a': (avgDelaysUs["ascon128a"]["0 dBm"],
                  avgDelaysUs["ascon128a"]["9 dBm"],
                  avgDelaysUs["ascon128a"]["20 dBm"]),
  'ASCON-128': (avgDelaysUs["ascon128"]["0 dBm"],
                avgDelaysUs["ascon128"]["9 dBm"],
                avgDelaysUs["ascon128"]["20 dBm"])
}

def bargraph():
  x = np.arange(len(TX_POWERS))
  width = 0.2
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')

  if RENDER_PGF:
    fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
    fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for attribute, measurement in toDisplay.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute,
                  color=cipherColors[attribute])

    if SHOW_BAR_LABELS:
      ax.bar_label(rects, padding=3)

    multiplier += 1

  ax.set_ylabel('Delay (μs)')
  ax.set_title('Average Delay')

  x_width_offset = 0.30
  ax.set_xticks(x + x_width_offset, TX_POWERS_LABELS.values())

  y_min = 0
  y_lim = 40000

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
  bargraph()

  if not RENDER_PGF:
    plt.show()