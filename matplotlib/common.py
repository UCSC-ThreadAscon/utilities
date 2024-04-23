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
            "9dbm": "csv/washingmachine/washingmachine-ascon12a8-9dbm.csv"
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
            "9dbm": "csv/secondstory-ascon128-9dbm.csv"
        },
        "ascon128": {
            "0dbm": "csv/secondstory/secondstory-ascon128-0dbm.csv",
            "20dbm": "csv/secondstory/secondstory-ascon128-20dbm.csv",
            "9dbm": "csv/secondstory/secondstory-ascon128-9dbm.csv"
        }
    }
}

cipherToColor = {
  'AES-CCM': 'deepskyblue',
  'ASCON-128a': 'plum',
  'ASCON-128': 'orange' 
}