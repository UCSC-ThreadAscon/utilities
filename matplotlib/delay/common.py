import os

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/ThesisWriteup/images/pgfs'
THESIS_PAPER_WIDTH_IN = 5.75113
THESIS_PAPER_HEIGHT_IN = 8.12659

CIPHERS = ["ascon128a", "ascon128", "aes", "no encryption"]
TX_POWERS = ["20 dBm", "9 dBm", "0 dBm"]

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

averageDelays = \
{
  "no encryption": {
    "20 dBm": "",
     "9 dBm": "",
     "0 dBm": ""
  },
  "aes": {},
  "ascon128a": {},
  "ascon128": {}
}