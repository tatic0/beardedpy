#python port of head

import sys
import argparse

"""
pure python implementation of the unix 'head' command
"""

# CLI options
parser = argparse.ArgumentParser(description='Print  the first 10 lines of each FILE to standard output..')
parser.add_argument('-n', '--lines', help='print the first N lines of FILE', type=int, dest='nlines')
parser.add_argument('-c', '--bytes', help='print the first K bytes of FILE', type=int, dest='nbytes')
parser.add_argument('-q', '--quiet', help='never print headers giving file names', action="store_true")
parser.add_argument('-v', '--verbose', help='always print headers giving file names', action="store_true")

arguments = parser.parse_args()

if arguments.verbose==True:
  print("verbose mode ON")

