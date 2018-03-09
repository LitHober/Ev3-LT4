#!/usr/bin/env python3
# So program can be run from Brickman

'''

'''

from ev3dev.ev3 import *
from time import sleep

mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=900)
mC.run_forever(speed_sp=900)
sleep(5)

mB.stop(stop_action="coast")
mC.stop(stop_action="coast")
sleep(5)
