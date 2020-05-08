#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pyfiglet import Figlet
from os.path import exists

__author__ = "Francesco Anselmo"
__copyright__ = "Copyright 2019, Francesco Anselmo"
__credits__ = ["Francesco Anselmo"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Francesco Anselmo"
__email__ = "francesco.anselmo@gmail.com"
__status__ = "Dev"

def lw2fabtotum(INPUT_FILENAME, OUTPUT_FILENAME, VERBOSE, DEBUG):
    if exists(INPUT_FILENAME):
        pass
    else:
        print("please provide an input LaserWeb gcode filename.")


def show_title():
    f1 = Figlet(font='standard')
    print(f1.renderText('lw2FABtotum'))

def main():

    show_title()

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="increase the verbosity level")
    parser.add_argument("-d", "--debug", action="store_true", help="print debug information")
    parser.add_argument("-i","--input", default="input.gcode", help="input gcode file name from LaserWeb")
    parser.add_argument("-o","--output", default="output.gcode", help="output gcode file name for the FABtotum")

    args = parser.parse_args()

    VERBOSE = args.verbose
    DEBUG = args.debug
    INPUT_FILENAME = args.input
    OUTPUT_FILENAME = args.output

    lw2fabtotum(INPUT_FILENAME, OUTPUT_FILENAME, VERBOSE, DEBUG)

if __name__ == "__main__":
    main()
