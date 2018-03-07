#!/usr/bin/python

import sys
from utils import generate_smallest_palindrome_bases


if len(sys.argv) != 3:
    print 'USAGE: ./generate_smallest_palindrome_bases.py [start number] [end number]'
else:
    generate_smallest_palindrome_bases(int(sys.argv[1]), int(sys.argv[2]))
