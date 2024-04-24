import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *

TX_POWERS = ["0dbm", "9dbm", "20dbm"]

def get_ratios(location, cipher):
  ratios = []
  for tx in TX_POWERS:
    value_cipher = getAvgMAh(prelimData[location][cipher][tx])
    value_aes = getAvgMAh(prelimData[location]["aes"][tx])
    ratio = 1 - (value_cipher / value_aes)
    ratio *= 100
    ratio *= -1
    ratios.append(ratio)
  return ratios


def linegraph(location, title):
  ascon128a_ratios = get_ratios(location, "ascon128a")
  ascon128_ratios = get_ratios(location, "ascon128")

  all_ratios = ascon128a_ratios + ascon128_ratios
  y_interval = 1.5
  y_lim = max(all_ratios) + y_interval
  y_min = min(all_ratios) - y_interval

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  ascon128a_lines = plt.plot(TX_POWERS, ascon128a_ratios, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascion128_lines = plt.plot(TX_POWERS, ascon128_ratios, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')

  ax.set_yticks(np.arange(y_min, y_lim, y_interval))
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('mAh difference between AES (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

  plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-ratio-sed.pgf'))

if __name__ == "__main__":
  linegraph('front-door', 'Front Door Sleepy End Device')
  linegraph('washing-machine', 'Washing Machine Sleepy End Device')
  linegraph('second-story', 'Second Story Sleepy End Device')
  # plt.show()