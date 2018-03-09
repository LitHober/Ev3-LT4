#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

# Connect EV3 color sensor and touch sensor
# and check they are connected.

cl = ColorSensor()
assert cl.connected, "Connect an EV3 color sensor to any sensor port"

ts = TouchSensor()
assert ts.connected, "Connect a touch sensor to any sensor port"

# Connect a large motor to port B and check it is connected.
m = LargeMotor('outB')
assert m.connected, "Connect a large motor to port B"

# Put the color sensor into COL-AMBIENT mode
# to measure ambient light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode='COL-AMBIENT'

# run_forever command will allow us to vary motor
# performance on the fly by adjusting speed_sp attribute.
m.run_forever(speed_sp = 0)

while not ts.value():    # Stop program by pressing touch sensor button
# set the motor's speed set point to be equal to
# the measured ambient light intensity value
    m.speed_sp = cl.value()

Sound.beep()
