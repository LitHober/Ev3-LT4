#!/usr/bin/env python3

from ev3dev.ev3 import *
from random import randint

#Sensores y motores
cl = ColorSensor('in3')
ir = InfraredSensor('in2') 
motorIzq = LargeMotor('outB')
motorDer = LargeMotor('outC')

#Modos
cl.mode = 'COL-COLOR'
ir.mode = 'IR-PROX'

#Variables
btn = Button()

while not btn.any():

    if ir.value() < 20:
        motorIzq.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
        motorDer.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake") 
        rumbo = random()
        if rumbo == 1:
            motorIzq.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
            motorDer.stop()
        else:
            motorIzq.stop()
            motorDer.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
    else:
        motorIzq.run_forever(speed_sp=200)
        motorDer.run_forever(speed_sp=200)

motorIzq.stop(stop_action='brake')
motorDer.stop(stop_action='brake')