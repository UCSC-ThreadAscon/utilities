import matplotlib.pyplot as plt
import numpy as np

from common import *

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 1)

ax = plt.axes()

y_lim = 100
ax.set_yticks(np.arange(0, y_lim + 10, 10))
ax.legend(loc='upper right', ncols=3)
ax.set_ylim(0, y_lim)

# red dashes, blue squares and green triangles
plt.plot([5, 10, 15], 'o--r', color=cipherToColor['AES-CCM'])
plt.plot([10, 20, 30], 'o:b', color=cipherToColor['ASCON-128a'])
plt.plot([30, 40, 60], 'o-.g', color=cipherToColor['ASCON-128'])

plt.show()