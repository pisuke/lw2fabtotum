;FABtotum laser cutting: test/four_squares_lw.gcode
G4 S1 ;1 millisecond pause to buffer the bep bep
M728 ;FABtotum bep bep
M793 S4 ;enable laser head
G90 ;use absolute coordinates
G4 S1 ;1 second pause to reach the printer (run fast)
G1 F10000 ;set initial travel speed
G21         ; Set units to mm
G90         ; Absolute positioning

;
; Operation:    0
; Type:         Laser Cut
; Paths:        4
; Passes:       1
; Cut rate:     1000 mm/min
;

; Macro [hookOperationStart]: LASER OFF
M5

; Macro [hookPassStart]: LASER OFF
M5


; Pass 0

; Pass 0 Path 0
M62 ;Turn off laser
G0 X51.00 Y102.00
M61 S255
G1 X1.00 Y102.00 S1.00 F1000
G1 X1.00 Y52.00
G1 X51.00 Y52.00
G1 X51.00 Y102.00
G1 X51.00 Y102.00

; Pass 0 Path 1
M62 ;Turn off laser
G0 X52.00 Y102.00
M61 S255
G1 X52.00 Y52.00 S1.00 F1000
G1 X102.00 Y52.00
G1 X102.00 Y102.00
G1 X52.00 Y102.00

; Pass 0 Path 2
M62 ;Turn off laser
G0 X52.00 Y51.00
M61 S255
G1 X52.00 Y1.00 S1.00 F1000
G1 X102.00 Y1.00
G1 X102.00 Y51.00
G1 X52.00 Y51.00

; Pass 0 Path 3
M62 ;Turn off laser
G0 X51.00 Y51.00
M61 S255
G1 X1.00 Y51.00 S1.00 F1000
G1 X1.00 Y1.00
G1 X51.00 Y1.00
G1 X51.00 Y51.00
G1 X51.00 Y51.00

; Macro [hookPassEnd]: LASER OFF
M5

; Macro [hookOperationEnd]: LASER OFF
M5
M5          ; Switch tool offEnd
M62 ;Turn off laser
