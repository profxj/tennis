#!/usr/bin/env python
"""
Setup match-ups for a Tourney
"""
from __future__ import (print_function, absolute_import, division, unicode_literals)

import pdb

try:  # Python 3
    ustr = unicode
except NameError:
    ustr = str

def parser(options=None):
    import argparse
    # Parse
    parser = argparse.ArgumentParser(description='Generate Tourney matchups')
    parser.add_argument("names", type=str, help="File providing the list of names in seeded order")
    parser.add_argument("--table_file", type=str, help="Generate Table with this filename")
    parser.add_argument("--json_file", type=str, help="Generate JSON file")
    #parser.add_argument("--sdss", default=False, action="store_true", help="Build SDSS bits and pieces too?")

    if options is None:
        pargs = parser.parse_args()
    else:
        pargs = parser.parse_args(options)
    return pargs


def main(pargs):
    """ Run
    """
    import warnings
    from IPython import embed
    from linetools import utils as ltu
    from tennis import tourney
    from tennis import io as tennis_io

    # Load seeds
    seeds = tennis_io.load_seeding(pargs.names)

    # Generate
    matches = tourney.generate_match_ups(seeds)

    # Write to JSON
    if pargs.json_file is not None:
        ltu.savejson(pargs.json_file, matches, overwrite=True, easy_to_read=True)
        print("Wrote: {:s}".format(pargs.json_file))

    # Table
    if pargs.table_file is not None:
        mtch_tbl = tourney.table_from_matches(matches)
        mtch_tbl.write(pargs.table_file, format='csv')






