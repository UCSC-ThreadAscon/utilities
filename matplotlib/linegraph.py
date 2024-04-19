import matplotlib.pyplot as plt
import numpy as np

from common import *

tx_powers = [-9, 0, 20]
y_lim = 15
y_min = -15
y_interval = 5

fig, ax = plt.subplots()

fig.set_figwidth(THESIS_PAPER_WIDTH_IN / 1.2)
fig.set_figheight(THESIS_PAPER_HEIGHT_IN / 3)

ascon128a_lines = plt.plot(tx_powers, [-8, -1, 13], 'o:',
                           color=cipherToColor['ASCON-128a'],
                           label='ASCON-128a')
ascion128_lines = plt.plot(tx_powers, [-9, -2, 12], 'o-.',
                           color=cipherToColor['ASCON-128'],
                           label='ASCON-128')

ax.set_yticks(np.arange(y_min, y_lim + 15, y_interval))
ax.set_xticks([-9, 0, 20])
ax.set_ylim(y_min, y_lim)

ax.legend(loc='best', ncols=3)
ax.set_ylabel('Energy Consumption Change from AES (%)')
ax.set_xlabel('TX Power (dBm)')
ax.set_title('Front Door ESP32-H2')

plt.axhline(linestyle='dotted', lw=1, color='gainsboro')

plt.savefig(os.path.join(THESIS_FIGURES_PATH, 'linegraph.pgf'))
# plt.show()