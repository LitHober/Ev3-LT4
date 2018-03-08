#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

mB = LargeMotor('outB')
mC = LargeMotor('outC')


mB.run_to_rel_pos(position_sp=720, speed_sp=450, stop_action="brake")
mC.run_to_rel_pos(position_sp=720, speed_sp=450, stop_action="brake")

mB.wait_while('running')
mC.wait_while('running')
    
sleep(1) # Wait one second


mB.run_to_rel_pos(position_sp=-720, speed_sp=450)
mC.run_to_rel_pos(position_sp=-720, speed_sp=450)

mB.wait_while('running')
mC.wait_while('running')
    
sleep(1) # Wait one second


mB.run_timed(time_sp=1000, speed_sp=450)
mC.run_timed(time_sp=1000, speed_sp=450)


mB.wait_while('running')
mC.wait_while('running')
