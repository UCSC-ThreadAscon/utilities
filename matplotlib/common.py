import matplotlib
import os

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

THESIS_FIGURES_PATH = '/Users/simeon/Desktop/Repositories/ThesisWriteup/images/pgfs'

"""
How long each experiment runs for in minutes, hours, and seconds.
"""
EXPERIMENT_RUNTIME_MINUTES = 183
EXPERIMENT_RUNTIME_HOURS = EXPERIMENT_RUNTIME_MINUTES / 60

files = {
    "front-door": {
        "aes": {
            "0dbm": "samples/aes-0dbm-frontdoor-sample.csv",
            "20dbm": "samples/aes-20dbm-frontdoor-sample.csv",
            "-9dbm": "samples/aes-neg9dbm-frontdoor-sample.csv"
        },
        "ascon128a": {
            "0dbm": "samples/libascon128a-0dbm-frontdoor.csv",
            "20dbm": "samples/libascon128a-20dbm-frontdoor.csv",
            "-9dbm": "samples/libascon128a-neg9dbm-frontdoor.csv"
        },
        "ascon128": {
            "0dbm": "samples/libascon128-0dbm-frontdoor.csv",
            "20dbm": "samples/libascon128-20dbm-frontdoor-sample.csv",
            "-9dbm": ""
        }
    },
    "washing-machine": {
        "aes": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128a": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        }
    },
    "second-story": {
        "aes": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128a": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        },
        "ascon128": {
            "0dbm": "",
            "20dbm": "",
            "-9dbm": ""
        }
    }
}

cipherToColor = {
  'AES-CCM': 'deepskyblue',
  'ASCON-128a': 'plum',
  'ASCON-128': 'orange' 
}