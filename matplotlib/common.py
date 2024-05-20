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
TX_POWERS_LABELS = {
  "0dbm": "0 dBm",
  "9dbm": "9 dBm",
  "20dbm": "20 dBm"
}

THROUGHPUT_EXP_PACKET_SIZE = 50
THROUGHPUT_EXP_PAYLOAD_SIZE = 4

DIR = "/Users/simeon/Desktop/Thesis/Final CSVs/"
files = {
  "front-door": {
    "aes": {
      "0dbm": os.path.join(DIR, "frontdoor-aes-0.csv"),
      "9dbm": os.path.join(DIR, "frontdoor-aes-9.csv"),
      "20dbm": os.path.join(DIR, "frontdoor-aes-20.csv")
    },
    "ascon128a": {
      "0dbm": os.path.join(DIR, "frontdoor-ascon128a-0.csv"),
      "9dbm": os.path.join(DIR, "frontdoor-ascon128a-9.csv"),
      "20dbm": os.path.join(DIR, "frontdoor-ascon128a-20.csv")
    },
    "ascon128": {
      "0dbm": os.path.join(DIR, "frontdoor-ascon128-0.csv"),
      "9dbm": os.path.join(DIR, "frontdoor-ascon128-9.csv"),
      "20dbm": os.path.join(DIR, "frontdoor-ascon128-20.csv")
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
            "0dbm": 31.924641735627052,
            "9dbm": 32.55737426586865,
            "20dbm": 33.90057606226406
        },
        "ascon128a": {
            "0dbm": 31.801013388165657,
            "9dbm": 32.467033060670914,
            "20dbm": 34.552977968148326
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 34.78780150981463
        }
    }
}

finalDataMaNoTrigger = {
    "front-door": {
        "aes": {
            "0dbm": 2.3678119519747614,
            "9dbm": 2.335702647417056,
            "20dbm": 2.2631310371666786
        },
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 2.188377776081277
        }
    }
}