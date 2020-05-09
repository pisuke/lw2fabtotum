# lw2fabtotum
[LaserWeb](https://github.com/LaserWeb/LaserWeb4/wiki) to [FABTotum](https://github.com/FABtotum) gcode conversion for laser cutting.

## Installation

### Pre-requisites

```
pip3 install -r requirements.txt
```

## Steps for generating a cutting gcode file compatible with the FABtotum

1. Create a CAD file and save it to R12 DXF file.
2. Load the file into [LaserWeb](https://github.com/LaserWeb/LaserWeb4) and save it to gcode.
3. Run lw2fabtotum:

```
$ python3 lw2fabtotum.py -i input_filename.gcode -o output_filename.gcode
```

4. Load the file into your FABtotum, put your sheet material on the tray and cut!

## Command line options

```
 _          ____  _____ _    ____  _        _
| |_      _|___ \|  ___/ \  | __ )| |_ ___ | |_ _   _ _ __ ___
| \ \ /\ / / __) | |_ / _ \ |  _ \| __/ _ \| __| | | | '_ ` _ \
| |\ V  V / / __/|  _/ ___ \| |_) | || (_) | |_| |_| | | | | | |
|_| \_/\_/ |_____|_|/_/   \_\____/ \__\___/ \__|\__,_|_| |_| |_|


usage: lw2fabtotum.py [-h] [-v] [-d] [-i INPUT] [-o OUTPUT] [-s SPEED]
                     [-p POWER]

optional arguments:
 -h, --help            show this help message and exit
 -v, --verbose         increase the verbosity level
 -d, --debug           print debug information
 -i INPUT, --input INPUT
                       input gcode file name from LaserWeb
 -o OUTPUT, --output OUTPUT
                       output gcode file name for the FABtotum
 -s SPEED, --speed SPEED
                       speed rate for laser head movement, it must be a
                       number between 1 and 20000
 -p POWER, --power POWER
                       laser head power, it must be a number between 1 and
                       255
```

## Reference

* [G codes for the FABtotum](https://github.com/Opentotum/Opentotum/wiki/G-Code)
* [FABlin G codes including the laser ones](http://fabtotum.github.io/FABlin/#File:Marlin_main.cpp:M61)
