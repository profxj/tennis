""" Module for codes related to the Tournament"""
from __future__ import absolute_import, division, print_function

import numpy as np

import pdb
from IPython import embed


def generate_match_ups(seeds, nround=3):
    """ """
    # Check divisible by 4
    if len(seeds) % 4 != 0:
        print("This method is expecting units of 4 players")
        embed()
    # Require even number of 4 for now
    ngroups = len(seeds) // 4
    if (ngroups % 2) != 0:
        print("Need even number of sets of 4")
        embed()

    # Matches
    matches = {}

    # Giddy up
    lbl_group = ['A','B','C','D','E','F']
    for round in range(nround):
        rkey = 'Round{:d}'.format(round+1)
        matches[rkey] = {}
        for group in range(ngroups//2):
            # Match top to bottom first and rotate
            off = (group + round) % (ngroups//2)
            # Pair
            pair_group = ngroups - off - 1
            # Draw the random players from upper seed
            rand = np.random.uniform(0,1,4)
            uidx = np.argsort(rand)
            # Draw for lower
            rand = np.random.uniform(0,1,4)
            lidx = np.argsort(rand)
            # Match-em up
            for ii,lbl in enumerate(['1a','1b','2a','2b']):
                key = lbl_group[group]+lbl
                matches[rkey][key] = [[seeds['Names'][group*4+uidx[ii]],
                                       seeds['Names'][pair_group*4+lidx[ii]]]]
    # Return
    return matches
