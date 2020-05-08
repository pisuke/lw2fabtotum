# lw2fabtotum
LaserWeb to FABTotum gcode conversion for laser cutting.

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

## Reference

* [G codes for the FABtotum](https://github.com/Opentotum/Opentotum/wiki/G-Code)
* [FABlin G codes including the laser ones](http://fabtotum.github.io/FABlin/#File:Marlin_main.cpp:M61)
