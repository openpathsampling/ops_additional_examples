#!/usr/bin/env python
from __future__ import print_function
import os
import argparse
import glob

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ipynb-directory', type=str, default='.',
                        help='directory to search for notebooks')
    parser.add_argument('--skip', nargs='+', type=str,
                        help='notebooks to skip')
    parser.add_argument('--skip-file', type=str,
                        help='file containing names of notebooks to skip')
    return parser

def base_filename(filename):
    return os.path.splitext(os.path.basename(filename))[0]

def find_all_ipynbs(directory):
    glob_str = os.path.join(directory, "*ipynb")
    ipynbs = set([base_filename(f) for f in glob.glob(glob_str)])
    return ipynbs

if __name__ == "__main__":
    parser = make_parser()
    opts = parser.parse_args()

    skip_long = opts.skip
    if skip_long is None:
        skip_long = []

    if opts.skip_file is not None:
        with open(opts.skip_file) as f:
            file_skips = f.read().splitlines()

        skip_long += file_skips

    skips = set([base_filename(f) for f in skip_long])

    ipynbs = find_all_ipynbs(opts.ipynb_directory)
    allowed = ipynbs - skips

    print(" ".join(list(allowed)))
