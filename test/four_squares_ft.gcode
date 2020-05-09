;FABtotum laser cutting: test/four_squares_lw.gcode
G4 S1 ;1 millisecond pause to buffer the bep bep
M728 ;FABtotum bep bep
M793 S4 ;enable laser head
G90 ;use absolute coordinates
G4 S1 ;1 second pause to reach the printer (run fast)
G1 F10000 ;set initial travel speed
M62 ;Turn off laser
G1 F10000
G0 X51.00 Y102.00
M61 S250
G1 X1.00 Y102.00 S1.00 F250
G1 X1.00 Y52.00
G1 X51.00 Y52.00
G1 X51.00 Y102.00
G1 X51.00 Y102.00
M62 ;Turn off laser
G1 F10000
G0 X52.00 Y102.00
M61 S250
G1 X52.00 Y52.00 S1.00 F250
G1 X102.00 Y52.00
G1 X102.00 Y102.00
G1 X52.00 Y102.00
M62 ;Turn off laser
G1 F10000
G0 X52.00 Y51.00
M61 S250
G1 X52.00 Y1.00 S1.00 F250
G1 X102.00 Y1.00
G1 X102.00 Y51.00
G1 X52.00 Y51.00
M62 ;Turn off laser
G1 F10000
G0 X51.00 Y51.00
M61 S250
G1 X1.00 Y51.00 S1.00 F250
G1 X1.00 Y1.00
G1 X51.00 Y1.00
G1 X51.00 Y51.00
G1 X51.00 Y51.00
M62 ;Turn off laser
