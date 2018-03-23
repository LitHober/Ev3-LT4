#!/usr/bin/env python3

from ev3dev.ev3 import *
import threading

#Sensores y motores
cl = ColorSensor('in3')
ir = InfraredSensor('in2') 
motorA = LargeMotor('outB')
motorB = LargeMotor('outC')

#Modos
cl.mode = 'COL-COLOR'
ir.mode = 'IR-PROX'

#Variables
btn = Button()
distance = ir.value()

def esquivar ():
    if distance < 20 :
        motorA.run_direct(duty_cycle_sp= -70, speed_sp=450)
        motorB.run_direct(duty_cycle_sp= -70, speed_sp=450)
        motorA.run_timed(time_sp=1000, speed_sp=600)
    else:
        motorA.run_direct(duty_cycle_sp= 100, speed_sp=200)
        motorB.run_direct(duty_cycle_sp= 100, speed_sp=200)


while not btn.any():
    hilo = threading.Thread( name = 'esquivar', target = esquivar )
    hilo.start()
motorA.stop(stop_action='brake')
motorB.stop(stop_action='brake')