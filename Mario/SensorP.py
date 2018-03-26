#!/usr/bin/env python3

from ev3dev.ev3 import *

ir = InfraredSensor() 
assert ir.connected, "Connect a single infrared sensor to any sensor port"

ir.mode = 'IR-PROX'

#Iniciar Motores
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while not btn.any():    
    distance = ir.value()

    if distance < 60:
        mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
		mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake")
    else:
    	mB.run_forever(speed_sp=150)
		mC.run_forever(speed_sp=150)
        
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
