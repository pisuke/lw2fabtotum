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

FABTOTUM_LASERCUTTING_HEADER = ''';FABtotum laser cutting: {}
G4 S1 ;1 millisecond pause to buffer the bep bep
M728 ;FAB bep bep
M793 S4; enable laser head
G90 ; absolute mode
G4 S1 ;1 second pause to reach the printer (run fast)
G1 F10000 ;Set initial travel speed
M61 S255 ;Finish moves and set laser power to maximum
'''


def lw2fabtotum(INPUT_FILENAME, OUTPUT_FILENAME, VERBOSE, DEBUG):
    if exists(INPUT_FILENAME):
        if not exists(OUTPUT_FILENAME):
            infile = open(INPUT_FILENAME, 'r')
            outfile = open(OUTPUT_FILENAME, 'w')
            output_text=FABTOTUM_LASERCUTTING_HEADER.format(INPUT_FILENAME)
            print(output_text)
            outfile.write(output_text)
            outfile.close()
            infile.close()
        else:
            print('the {} file already exists, please delete it or provide a different filename'.format(OUTPUT_FILENAME))
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
