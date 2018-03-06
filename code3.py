#!/usr/bin/env python3

from ev3dev.ev3 import *

btn = Button()

cS = ColorSensor()

cS.mode = 'COL-REFLECT'


motorA = LargeMotor('outB')
motorB = LargeMotor('outC')

motorA.inversed(speed_sp=200)
motorB.inversed(speed_sp=200)






#negro 4
#azul 11
#cafe 30
#rojo 57

 
