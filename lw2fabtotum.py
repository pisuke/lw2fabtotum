#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import validators
from pyfiglet import Figlet
from os.path import exists
from sys import exit

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
'''

FABTOTUM_LASERCUTTING_FOOTER = '''M62 ;Turn off laser
'''

def lw2fabtotum(INPUT_FILENAME, OUTPUT_FILENAME, SPEED, POWER, VERBOSE, DEBUG):
    """convert the LaserWeb G Code file to a FABtotum G Code file.

    Arguments:
        INPUT_FILENAME {[string]} -- input gcode file name from LaserWeb
        OUTPUT_FILENAME {[string]} -- output gcode file name for the FABtotum
        SPEED {[integer]} -- speed rate for laser head movement, it must be a number between 1 and 20000
        POWER {[integer]} -- laser head power, it must be a number between 1 and 255
        VERBOSE {[boolean]} -- increase the verbosity level
        DEBUG {[boolean]} -- print debug information

    """
    if exists(INPUT_FILENAME):
        if not exists(OUTPUT_FILENAME):
            infile = open(INPUT_FILENAME, 'r')
            outfile = open(OUTPUT_FILENAME, 'w')
            output_text=FABTOTUM_LASERCUTTING_HEADER.format(INPUT_FILENAME)
            for line in infile.readlines():
                # disable laser head power for non cutting motion
                if line[0:2]=="G0":
                    output_text+="M62 ;Turn off laser\n"
                    output_text+=line
                    output_text+="M61 S{}\n".format(POWER)
                else:
                    output_text+=line
                # replace laser head speed with user selected one


            output_text+=(FABTOTUM_LASERCUTTING_FOOTER)
            if DEBUG:
                print(output_text)
            outfile.write(output_text)
            outfile.close()
            infile.close()
            print("conversion completed to output file {}".format(OUTPUT_FILENAME))
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
    parser.add_argument("-s","--speed", default="500", help="speed rate for laser head movement, it must be a number between 1 and 20000")
    parser.add_argument("-p","--power", default="255", help="laser head power, it must be a number between 1 and 255")

    args = parser.parse_args()

    if not validators.between (int(args.speed), min=1, max=20000):
        print("laser head speed must be between 1 and 20000")
        exit(1)

    if not validators.between (int(args.power), min=1, max=255):
        print("laser head power must be between 1 and 255")
        exit(1)

    lw2fabtotum(args.input, args.output, args.speed, args.power, args.verbose, args.debug)

if __name__ == "__main__":
    main()
