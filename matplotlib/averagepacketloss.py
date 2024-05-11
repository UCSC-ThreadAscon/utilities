import matplotlib.pyplot as plt
import numpy as np

from common import *
from average import *
from packetloss import *

TX_POWERS = ["0dbm", "9dbm", "20dbm"]

def get_average_packet_losses(cipher):
  average_packet_losses = [0, 0, 0]

  for location in LOCATIONS_ENERGY:
    packet_losses = getPacketLoss(location, cipher)

    for i in range(0, 3):
      average_packet_losses[i] += packet_losses[i]
  
  for i in range(0, 3):
    average_packet_losses[i] /= 3

  return average_packet_losses


def average_packet_losses(title):
  aes = get_average_packet_losses('aes')
  ascon128 = get_average_packet_losses('ascon128')
  ascon128a = get_average_packet_losses('ascon128a')

  all_ratios = aes + ascon128 + ascon128a
  # y_interval = 15
  # y_lim = max(all_ratios) + y_interval
  # y_min = min(all_ratios) - y_interval

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

  plt.savefig(os.path.join(THESIS_FIGURES_PATH, f'average-packet-loss.pgf'))

if __name__ == "__main__":
  average_packet_losses("All Full Thread Devices")
  # plt.show()
  pass