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

#python port of head


#Usage: head [OPTION]... [FILE]...
#Print the first 10 lines of each FILE to standard output.
#With more than one FILE, precede each with a header giving the file name.
#With no FILE, or when FILE is -, read standard input.
#
#Mandatory arguments to long options are mandatory for short options too.
#  -c, --bytes=[-]K         print the first K bytes of each file;
#                             with the leading '-', print all but the last
#                             K bytes of each file
#  -n, --lines=[-]K         print the first K lines instead of the first 10;
#                             with the leading '-', print all but the last
#                             K lines of each file
#  -q, --quiet, --silent    never print headers giving file names
#  -v, --verbose            always print headers giving file names
#      --help     display this help and exit
#      --version  output version information and exit
#
#K may have a multiplier suffix:
#b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
#GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.


import sys
#import linecache ## finally, not a good idea

inputfile = sys.argv[1]
linestoread = int(sys.argv[2])

rawdata = open(inputfile, 'r')

for i in range(0,linestoread):
  print(rawdata.readline().rstrip())

