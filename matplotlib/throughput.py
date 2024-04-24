import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *

TX_POWERS = ["0dbm", "9dbm", "20dbm"]

PACKET_SIZE = 50

def get_throughputs(location, cipher):
  throughputs = []
  for tx in TX_POWERS:
    throughput = averageRTTs[location][cipher][tx]
    throughputs.append(throughput)
  return throughputs


def throughput(location, title):
  aes = get_throughputs(location, 'aes')
  ascon128 = get_throughputs(location, 'ascon128')
  ascon128a = get_throughputs(location, 'ascon128a')

  all_ratios = aes + ascon128 + ascon128a
  y_interval = 10
  y_lim = max(all_ratios) + y_interval
  y_min = min(all_ratios) - y_interval

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  aes_lines = plt.plot(TX_POWERS, aes, 'o--',
                      color=cipherToColor['AES-CCM'],
                      label='AES')
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
  ax.set_ylabel('Throughput (bytes / ms)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-throughput.pgf'))

if __name__ == "__main__":
  throughput('front-door', 'Front Door Full Thread Device')
  plt.show()
  pass