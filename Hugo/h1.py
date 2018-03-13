#!/usr/bin/env python3
from ev3dev.ev3 import *

btn = Button() # will use any button to stop script

# Sensor de color
cS = ColorSensor('in4')
cS.mode = 'COL-COLOR'

# Sensor de proximidad
iS = InfraredSensor('in1') 
iS.mode = 'IR-PROX'

motorA = LargeMotor('outB')
motorB = LargeMotor('outC')

while not btn.any():
    if iS.value()<20:
        motorA.run_to_rel_pos(position_sp=-720, speed_sp=450)
        motorB.run_to_rel_pos(position_sp=-720, speed_sp=450)
        motorA.run_to_rel_pos(position_sp=900, speed_sp=900)
        motorB.run_to_rel_pos(position_sp=-900, speed_sp=900)
    else:
        motorA.run_forever(speed_sp=300)
        motorB.run_forever(speed_sp=300)


mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
