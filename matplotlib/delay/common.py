import os

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/ThesisWriteup/images/pgfs'
THESIS_PAPER_WIDTH_IN = 5.75113
THESIS_PAPER_HEIGHT_IN = 8.12659

CIPHERS = ["ascon128a", "ascon128", "aes", "no encryption"]
TX_POWERS = ["20 dBm", "9 dBm", "0 dBm"]
NETWORK_TIME_SYNC_PERIOD_SECONDS = 30

RENDER_LATEX = False

if RENDER_LATEX:
  import matplotlib
  matplotlib.use("pgf")
  matplotlib.rcParams.update({
      "pgf.texsystem": "pdflatex",
      'font.family': 'serif',
      'text.usetex': True,
      'pgf.rcfonts': False,
  })

""" The average delays for each experiment are
    in microseconds (us).
"""
avgDelaysUs = \
{
  "no encryption": {
     "0 dBm": 20770,
     "9 dBm": 19606,
    "20 dBm": 20633
  },
  "ascon128": {
     "0 dBm": 25420,
     "9 dBm": 19262,
    "20 dBm": 19588
  },
  "ascon128a": {
    "0 dBm": 20607,
    "9 dBm": 21644,
    "20 dBm": 19449
  },
  "aes": {
    "0 dBm": 38225,
    "9 dBm": 25461,
    "20 dBm": 25155
  }
}