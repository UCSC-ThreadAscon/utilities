import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *
from throughput import *

def get_throughput_ratios(location, cipher):
  ratios = []
  for tx in TX_POWERS:
    throughput_cipher = averageRTTs[location][cipher][tx]
    throughput_aes = averageRTTs[location]["aes"][tx]

    ratio = 1 - (throughput_cipher / throughput_aes)
    ratio *= 100
    ratio *= -1
    ratios.append(ratio)
  return ratios

def throughput_ratios(location, title):
  ascon128 = get_throughput_ratios(location, 'ascon128')
  ascon128a = get_throughput_ratios(location, 'ascon128a')

  all_ratios = ascon128 + ascon128a
  y_interval = 10
  y_lim = 100
  y_min = -30

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  ascon128a_lines = plt.plot(TX_POWERS, ascon128a, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascion128_lines = plt.plot(TX_POWERS, ascon128, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')

  ax.set_yticks(np.arange(y_min, y_lim, y_interval))
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('Throughput difference between AES (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-ratio-throughput.pgf'))


if __name__ == "__main__":
  throughput_ratios('washing-machine', "Water Leakage Detector")
  throughput_ratios('front-door', "Bedroom Smart Plug")
  throughput_ratios('second-story', "Second Story Room Smart Plug")
  plt.show()