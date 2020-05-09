G21         ; Set units to mm
G90         ; Absolute positioning

;
; Operation:    0
; Type:         Laser Cut
; Paths:        4
; Passes:       1
; Cut rate:     1000 mm/min
;

; Pass 0

; Pass 0 Path 0
G0 X51.00 Y102.00
G1 X1.00 Y102.00 S1.00 F1000
G1 X1.00 Y52.00
G1 X51.00 Y52.00
G1 X51.00 Y102.00
G1 X51.00 Y102.00

; Pass 0 Path 1
G0 X52.00 Y102.00
G1 X52.00 Y52.00 S1.00 F1000
G1 X102.00 Y52.00
G1 X102.00 Y102.00
G1 X52.00 Y102.00

; Pass 0 Path 2
G0 X52.00 Y51.00
G1 X52.00 Y1.00 S1.00 F1000
G1 X102.00 Y1.00
G1 X102.00 Y51.00
G1 X52.00 Y51.00

; Pass 0 Path 3
G0 X51.00 Y51.00
G1 X1.00 Y51.00 S1.00 F1000
G1 X1.00 Y1.00
G1 X51.00 Y1.00
G1 X51.00 Y51.00
G1 X51.00 Y51.00
