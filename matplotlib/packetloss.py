import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *


def packetLoss(location, title):
  aes = getPacketLoss(location, 'aes')
  ascon128 = getPacketLoss(location, 'ascon128')
  ascon128a = getPacketLoss(location, 'ascon128a')

  y_interval = 1
  y_lim = 2
  y_min = -2

  ticks = np.arange(y_min, y_lim, y_interval)
  ticks = np.append(ticks, [y_lim])

  fig, ax = plt.subplots()

  # fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
  # fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

  aes_lines = plt.plot(TX_POWERS, aes, 'o--',
                      color=cipherToColor['AES-CCM'],
                      label='AES-CCM')
  ascon128a_lines = plt.plot(TX_POWERS, ascon128a, 'o:',
                            color=cipherToColor['ASCON-128a'],
                            label='ASCON-128a')
  ascion128_lines = plt.plot(TX_POWERS, ascon128, 'o-.',
                            color=cipherToColor['ASCON-128'],
                            label='ASCON-128')

  ax.set_yticks(ticks)
  ax.set_xticks(TX_POWERS)
  ax.set_ylim(y_min, y_lim)

  ax.legend(loc='best', ncols=3)
  ax.set_ylabel('Packet Loss (%)')
  ax.set_xlabel('TX Power (dBm)')
  ax.set_title(title)

  # plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'{location}-packet-loss.pgf'))

if __name__ == "__main__":
  packetLoss('washing-machine', "Water Leakage Detector")
  packetLoss('bedroom', "Bedroom Smart Plug")
  packetLoss('second-story', "Second Story Room Smart Plug")
  plt.show()