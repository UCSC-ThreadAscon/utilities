import matplotlib
import os

# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/ThesisWriteup/images/pgfs'
THESIS_PAPER_WIDTH_IN = 5.75113
THESIS_PAPER_HEIGHT_IN = 8.12659

EXPERIMENT_RUNTIME_MINUTES = 190
EXPERIMENT_RUNTIME_HOURS = EXPERIMENT_RUNTIME_MINUTES / 60

LOCATIONS_ENERGY = ["front-door", "air-quality", "second-story"]
LOCATIONS_THROUGHPUT = ["bedroom", "washing-machine", "second-story"]
CIPHERS = ["aes", "ascon128a", "ascon128"]
TX_POWERS = ["0dbm", "9dbm", "20dbm"]

THROUGHPUT_EXP_PACKET_SIZE = 50
THROUGHPUT_EXP_PAYLOAD_SIZE = 4

DIR = "/Users/simeon/Desktop/Thesis/Final CSVs/"
files = {
  "front-door": {
    "aes": {
      "0dbm": os.path.join(DIR, "frontdoor-aes-0.csv"),
      "9dbm": os.path.join(DIR, "frontdoor-aes-9.csv"),
      "20dbm": os.path.join(DIR, "frontdoor-aes-20.csv")
    }
  },
  "air-quality": {
    "aes": {
      "0dbm": os.path.join(DIR, "airquality-aes-0.csv"),
      "9dbm": os.path.join(DIR, "airquality-aes-9.csv"),
      "20dbm": os.path.join(DIR, "airquality-aes-20.csv")
    }
  },
  "second-story": {
    "aes": {
      "0dbm": os.path.join(DIR, "secondstory-aes-0.csv"),
      "9dbm": os.path.join(DIR, "secondstory-aes-9.csv"),
      "20dbm": os.path.join(DIR, "secondstory-aes-20.csv")
    }
  }
}

cipherToColor = {
  'AES-CCM': 'deepskyblue',
  'ASCON-128a': 'plum',
  'ASCON-128': 'orange' 
}

finalDataMa = {
    "front-door": {
        "aes": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        }
    }
}