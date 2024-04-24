import matplotlib
import os

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

THESIS_PAPER_WIDTH_IN = 5.75113
THESIS_PAPER_HEIGHT_IN = 8.12659

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/ThesisWriteup/images/pgfs'

"""
How long each experiment runs for in minutes, hours, and seconds.
"""
EXPERIMENT_RUNTIME_MINUTES = 183
EXPERIMENT_RUNTIME_HOURS = EXPERIMENT_RUNTIME_MINUTES / 60

files = {
    "front-door": {
        "aes": {
            "0dbm": "csv/front-door/front-door-aes-0dbm.csv",
            "20dbm": "csv/front-door/front-door-aes-20dbm.csv",
            "9dbm": "csv/front-door/front-door-aes-9dbm.csv"
        },
        "ascon128a": {
            "0dbm": "csv/front-door/front-door-ascon128a-0dbm.csv",
            "20dbm": "csv/front-door/front-door-ascon128a-20dbm.csv",
            "9dbm": "csv/front-door/front-door-ascon128a-9dbm.csv"
        },
        "ascon128": {
            "0dbm": "csv/front-door/front-door-ascon128-0dbm.csv",
            "20dbm": "csv/front-door/front-door-ascon128-20dbm.csv",
            "9dbm": "csv/front-door/front-door-ascon128-9dbm.csv"
        }
    },
    "washing-machine": {
        "aes": {
            "0dbm": "csv/washingmachine/washingmachine-aes-0dbm.csv",
            "20dbm": "csv/washingmachine/washingmachine-aes-20dbm.csv",
            "9dbm": "csv/washingmachine/washingmachine-aes-9dbm.csv"
        },
        "ascon128a": {
            "0dbm": "csv/washingmachine/washingmachine-ascon128a-0dbm.csv",
            "20dbm": "csv/washingmachine/washingmachine-ascon128a-20dbm.csv",
            "9dbm": "csv/washingmachine/washingmachine-ascon128a-9dbm.csv"
        },
        "ascon128": {
            "0dbm": "csv/washingmachine/washingmachine-ascon128-0dbm.csv",
            "20dbm": "csv/washingmachine/washingmachine-ascon128-20dbm.csv",
            "9dbm": "csv/washingmachine/washingmachine-ascon128-9dbm.csv"
        }
    },
    "second-story": {
        "aes": {
            "0dbm": "csv/secondstory/secondstory-aes-0dbm.csv",
            "20dbm": "csv/secondstory/secondstory-aes-20dbm.csv",
            "9dbm": "csv/secondstory/secondstory-aes-9dbm.csv"
        },
        "ascon128a": {
            "0dbm": "csv/secondstory/secondstory-ascon128a-0dbm.csv",
            "20dbm": "csv/secondstory/secondstory-ascon128a-20dbm.csv",
            "9dbm": "csv/secondstory/secondstory-ascon128-9dbm.csv"
        },
        "ascon128": {
            "0dbm": "csv/secondstory/secondstory-ascon128-0dbm.csv",
            "20dbm": "csv/secondstory/secondstory-ascon128-20dbm.csv",
            "9dbm": "csv/secondstory/secondstory-ascon128-9dbm.csv"
        }
    }
}

prelimData = {
    "washing-machine": {
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
    "washing-machine": {
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