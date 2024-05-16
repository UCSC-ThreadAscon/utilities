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

LOCATIONS_ENERGY = ["front-door", "air-quality", "second-story"]
LOCATIONS_THROUGHPUT = ["bedroom", "washing-machine", "second-story"]
CIPHERS = ["aes", "ascon128a", "ascon128"]
TX_POWERS = ["0dbm", "9dbm", "20dbm"]

THROUGHPUT_EXP_PACKET_SIZE = 50
THROUGHPUT_EXP_PAYLOAD_SIZE = 4

TEST_DIR = "/Users/simeon/Desktop/Thesis/Archive/CSV/"
testFiles = {
  "front-door": {
    "aes": {
      "9dbm": os.path.join(TEST_DIR, "frontdoor-aes-9.csv"),
      "20dbm": os.path.join(TEST_DIR, "frontdoor-aes-20.csv")
    },
  },
  "second-story": {
    "aes": {
      "9dbm": os.path.join(TEST_DIR, "secondstory-aes-9.csv"),
      "20dbm": os.path.join(TEST_DIR, "secondstory-aes-20.csv")
    }
  },
  "air-quality": {
    "aes": {
      "9dbm": os.path.join(TEST_DIR, "airquality-aes-9.csv"),
      "20dbm": os.path.join(TEST_DIR, "airquality-aes-20.csv")
    }
  }
}

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

finalData = {
    "air-quality": {
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "aes": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        }
    },
    "second-story": {
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "aes": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        }
    },
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

testMaAll = {
    "air-quality": {
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "aes": {
            "0dbm": 0,
            "9dbm": 2.350501575428397,
            "20dbm": 2.386913245115555
        }
    },
    "second-story": {
        "ascon128a": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "ascon128": {
            "0dbm": 0,
            "9dbm": 0,
            "20dbm": 0
        },
        "aes": {
            "0dbm": 0,
            "9dbm": 2.215943188145589,
            "20dbm": 2.180619549829353
        }
    },
    "front-door": {
        "aes": {
            "0dbm": 0,
            "9dbm": 2.17115823166256,
            "20dbm": 2.234762399107365
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