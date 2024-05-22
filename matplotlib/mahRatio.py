import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *


def linegraph(location, title):
  ascon128a_ratios = getMahRatios(location, "ascon128a")
  ascon128_ratios = getMahRatios(location, "ascon128")
  aes_ratios = getMahRatios(location, "aes")

  y_interval = 0.5
  y_lim = 10
  y_min = -2

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  ascon128a_lines = plt.plot(TX_POWERS, ascon128a_ratios, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascon128_lines = plt.plot(TX_POWERS, ascon128_ratios, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')
  aes_lines = plt.plot(TX_POWERS, aes_ratios, 'o--',
                            color=cipherToColor['AES-CCM'],
                            label='AES-CCM')

  y_ticks = np.arange(y_min, y_lim, y_interval)
  y_ticks = np.append(y_ticks, [100])
  ax.set_yticks(y_ticks)
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('mAh difference between No Encryption (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-ratio-sed.pgf'))

if __name__ == "__main__":
  linegraph('front-door', "Front Door Motion Sensor")
  plt.show()