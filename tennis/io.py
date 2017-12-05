""" Module for I/O related to tennis
"""
from __future__ import absolute_import, division, print_function

from astropy.table import Table

def load_seeding(seeding_file):
    # Load em up
    seeds = Table.read(seeding_file, format='ascii', guess=False)
    # Return
    return seeds

