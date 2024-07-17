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
  xAxisValues = np.arange(len(TX_POWERS))
  width = 0.2
  multiplier = 0

  figure, axis = plt.subplots(layout='constrained')

  if RENDER_PGF:
    figure.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
    figure.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  for cipher, delaysUs in toDisplay.items():

    delaysMs = [usToMs(delay) for delay in delaysUs]
    offset = width * multiplier
    rects = axis.bar(xAxisValues + offset, delaysMs, width, label=cipher,
                  color=cipherColors[cipher])

    if SHOW_BAR_LABELS:
      axis.bar_label(rects, padding=3)

    multiplier += 1

  axis.set_ylabel('Delay (ms)')
  axis.set_title('Average Delay')

  xWidthOffset = 0.30
  axis.set_xticks(xAxisValues + xWidthOffset, TX_POWERS_LABELS.values())

  y_min = 0
  y_lim = 40

  num_ticks = abs(y_lim - y_min) / 10
  ticks = np.arange(0, y_lim, num_ticks)
  ticks = np.append(ticks, [y_lim])

  axis.set_yticks(ticks)
  axis.legend(loc='best', ncols=4)
  axis.set_ylim(y_min, y_lim)

  axis.set_xlabel('TX Power (dBm)')

  if RENDER_PGF:
    plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'delay-bar-graph-mA.pgf'))
  return

if __name__ == "__main__":
  bargraph()

  if not RENDER_PGF:
    plt.show()