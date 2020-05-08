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
M728 ;FABtotum bep bep
M793 S4 ;enable laser head
G90 ;use absolute coordinates
G4 S1 ;1 second pause to reach the printer (run fast)
G1 F10000 ;set initial travel speed
M61 S255 ;finish moves and set laser power to maximum
'''

FABTOTUM_LASERCUTTING_FOOTER = '''M62 ;Turn off laser
'''

def lw2fabtotum(INPUT_FILENAME, OUTPUT_FILENAME, VERBOSE, DEBUG):
    """convert the LaserWeb G Code file to a FABtotum G Code file.

    Arguments:
        INPUT_FILENAME {[string]} -- [description]
        OUTPUT_FILENAME {[string]} -- [description]
        VERBOSE {[boolean]} -- [description]
        DEBUG {[boolean]} -- [description]
    """    
    if exists(INPUT_FILENAME):
        if not exists(OUTPUT_FILENAME):
            infile = open(INPUT_FILENAME, 'r')
            outfile = open(OUTPUT_FILENAME, 'w')
            output_text=FABTOTUM_LASERCUTTING_HEADER.format(INPUT_FILENAME)
            for line in infile.readlines():
                if line[0:2]=="G0":
                    output_text+="M62 ;Turn off laser\n"
                    output_text+=line
                    output_text+="M61 S255\n"
                else:
                    output_text+=line
            if DEBUG:
                print(output_text)
            outfile.write(output_text)
            outfile.close()
            infile.close()
        else:
            print('the {} file already exists, please delete it or provide a different filename'.format(OUTPUT_FILENAME))
    else:
        print("please provide an input LaserWeb gcode filename.")


def show_title():
    """show the program title
    """    
    f1 = Figlet(font='standard')
    print(f1.renderText('lw2FABtotum'))

def main():

    show_title()

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", default=False, help="increase the verbosity level")
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="print debug information")
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
