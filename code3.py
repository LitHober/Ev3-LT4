#!/usr/bin/env python3

from ev3dev.ev3 import *

btn = Button()

cS = ColorSensor()

cS.mode = 'COL-REFLECT'


motorA = LargeMotor('outB')
motorB = LargeMotor('outC')

motorA.run_forever(speed_sp=200)
motorB.run_forever(speed_sp=200)

while not btn.any():
    if cS.value()<9:
        Sound.speak('This is a trash!')
    elif cS.value()>10:
        motorA.inversed(speed_sp=200)
        motorB.inversed(speed_sp=200)
    else:
        motorA.run_forever(speed_sp=100)
        motorB.run_forever(speed_sp=100)




#negro 4
#azul 11
#cafe 30
#rojo 57

 
