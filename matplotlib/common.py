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

EXPERIMENT_RUNTIME_MINUTES = 183
EXPERIMENT_RUNTIME_HOURS = EXPERIMENT_RUNTIME_MINUTES / 60

LOCATIONS = ["front-door", "air-quality", "second-story"]
CIPHERS = ["aes", "ascon128a", "ascon128"]
TX_POWERS = ["0dbm", "9dbm", "20dbm"]

prelimData = {
    "air-quality": {
        "ascon128a": {
            "0dbm": 2.189051048110373,
            "9dbm": 2.2009832102270197,
            "20dbm": 2.2657710937696622
        },
        "ascon128": {
            "0dbm": 2.230416640867781,
            "9dbm": 2.43219885094373,
            "20dbm": 2.2951756211553045
        },
        "aes": {
            "0dbm": 2.197011395537738,
            "9dbm": 2.186341411404778,
            "20dbm": 2.2767459467587985
        }
    },
    "second-story": {
        "ascon128a": {
            "0dbm": 2.2673584616878375,
            "9dbm": 2.2138504941079695,
            "20dbm": 2.2594755837555778
        },
        "ascon128": {
            "0dbm": 2.1950598460887356,
            "9dbm": 2.2138504941079695,
            "20dbm": 2.2711082160520837
        },
        "aes": {
            "0dbm": 2.199091544891243,
            "9dbm": 2.2953161607213555,
            "20dbm": 2.332562045342504
        }
    },
    "front-door": {
        "aes": {
            "0dbm": 2.6163947354540644,
            "9dbm": 2.5245085198700314,
            "20dbm": 2.5389641009762656
        },
        "ascon128a": {
            "0dbm": 2.4736160593588976,
            "9dbm": 2.491912481377145,
            "20dbm": 2.550465063083697
        },
        "ascon128": {
            "0dbm": 2.808074486321598,
            "9dbm": 2.4829457013603187,
            "20dbm": 2.547015249453203
        }
    }
}

cipherToColor = {
  'AES-CCM': 'deepskyblue',
  'ASCON-128a': 'plum',
  'ASCON-128': 'orange' 
}

averageRTTs = {
    "air-quality": {
        "aes": {
            "0dbm": 42.743,
            "9dbm": 41.800,
            "20dbm": 41.116
        },
        "ascon128": {
            "0dbm": 58.244,
            "9dbm": 41.23,
            "20dbm": 40.463
        },
        "ascon128a": {
            "0dbm": 53.410,
            "9dbm": 42.166,
            "20dbm": 40.555
        }
    },
    "second-story": {
        "aes": {
            "0dbm": 55.393,
            "9dbm": 41.183,
            "20dbm": 41.916
        },
        "ascon128": {
            "0dbm": 42.313,
            "9dbm": 41.673,
            "20dbm": 45.536
        },
        "ascon128a": {
            "0dbm": 46.590,
            "9dbm": 45.346,
            "20dbm": 41.440
        }
    },
    "front-door": {
        "aes": {
            "0dbm": 50.531,
            "9dbm": 44.313,
            "20dbm": 44.126
        },
        "ascon128": {
            "0dbm": 52.929,
            "9dbm": 46.973,
            "20dbm": 42.586
        },
        "ascon128a": {
            "0dbm": 46.736,
            "9dbm": 43.943,
            "20dbm": 49.860
        }
    }
}

packetLossPercentagae = {
    "air-quality": {
        "aes": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0.3,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0.3
        }
    },
    "second-story": {
        "aes": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        }
    },
    "front-door": {
        "aes": {
            "0dbm": 1.0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 1.0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        }
    }
}