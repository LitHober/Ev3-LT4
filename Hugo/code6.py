#!/usr/bin/env python3

from ev3dev.ev3 import *

btn = Button()

# Sensor de color
cS = ColorSensor('in4')
cS.mode = 'COL-COLOR'

# Sensor de proximidad
iS = InfraredSensor('in1') 
iS.mode = 'IR-PROX'

motorA = LargeMotor('outB')
motorB = LargeMotor('outC')

motorA.run_forever(speed_sp=150)
motorB.run_forever(speed_sp=150)

while not btn.any():
    if iS.value()<20:
        motorA.run_to_rel_pos(position_sp=-720, speed_sp=450)
        motorB.run_to_rel_pos(position_sp=-720, speed_sp=450)
    

motorA.stop(stop_action='brake')
motorB.stop(stop_action='brake')


#negro 4
#azul 11
#cafe 30
#rojo 57