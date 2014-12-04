'''
Produces a list of banks along with all of the files that reference that bank
'''

import os, stat
from itertools import groupby
from collections import defaultdict

APPROVED_EXTS = ['.dcs']
SOUND_ACTION_NAME = 'tActionSound'
SND_PREFIX = 'SND_'


def all_dcs_files():
    for root, dirs, files in os.walk( '.' ):
        for name in files:
            base, ext = os.path.splitext(name)
            if ext.lower() not in APPROVED_EXTS:
                continue
            yield os.path.abspath(os.path.join(root, name))


def get_banks_in_file(filename):
    with open(filename, 'r') as f:
        sound_lines = [line for line in f if SOUND_ACTION_NAME in line]
        for line in sound_lines:
            for bank_name in [part.replace('SND_', '') for part in line.split('"') if SND_PREFIX in part]:
                yield bank_name


def go():
    filename_to_banks = {filename: get_banks_in_file(filename) for filename in all_dcs_files()}
    filename_to_bank = [(filename, b) for b in banks for filename, banks in filename_to_banks.iteritems()]
    bank_to_filenames = groupby(filename_to_bank, key=lambda x: x[1])
    for bank, filenames in bank_to_filenames:
        print "{}: {}".format(bank, '\t'.join(filenames))
