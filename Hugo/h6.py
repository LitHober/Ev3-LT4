#!/usr/bin/env python3

from ev3dev.ev3 import *

btn = Button()

# Sensor de color

cS = ColorSensor('in3')
cS.mode = 'COL-COLOR'

# Sensor de proximidad

ir = InfraredSensor('in2') 
ir.mode = 'IR-PROX'

motorA = LargeMotor('outB')
motorB = LargeMotor('outC')

motorA.run_forever(speed_sp=150)
motorB.run_forever(speed_sp=150)

distance = ir.value()


def esquivar ( distance ):

    if distance < 20 :

        motorA.run_direct(duty_cycle_sp= -70, speed_sp=450)
        motorB.run_direct(duty_cycle_sp= -70, speed_sp=450)
        motorA.run_timed(time_sp=1000, speed_sp=600)

while not btn.any():

 esquivar ( distance )

motorA.stop(stop_action='brake')
motorB.stop(stop_action='brake')