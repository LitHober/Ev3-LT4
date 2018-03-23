#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

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
distance = ir.value()

while not btn.any():
    if ir.value()<20:
        motorDer.stop()
        motorIzq.stop()
        motorDer.run_timed(time_sp=200, speed_sp=300)
        
    else:
        motorIzq.run_forever(speed_sp=300)
        motorDer.run_forever(speed_sp=300)

motorIzq.stop(stop_action='brake')
motorDer.stop(stop_action='brake')