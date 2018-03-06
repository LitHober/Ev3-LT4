#!usr/bin/env python3
from ev3dev.ev3 import*

btn = Button()

cl = ColorSensor()

cl.mode = 'COL-REFLECT'

mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=100)
mC.run_forever(speed_sp=100)

while not btn.any():
  if cl.value()<30:
    mB.stop(stop_action='brake')
    mC.stop(stop_action='brake')
    
  else:
    mB.stop(stop_action='brake')
    mC.stop(stop_action='brake')
    
# mB.stop(stop_action='break')
# mC.stop(stop_action='break')
