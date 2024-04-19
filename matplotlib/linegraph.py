import matplotlib.pyplot as plt
import numpy as np

from common import *

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 1)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'o--r', color=cipherToColor['AES-CCM'])
plt.plot(t, t**2, 'o:b', color=cipherToColor['ASCON-128a'])
plt.plot(t, t**3, 'o-.g', color=cipherToColor['ASCON-128'])
plt.show()