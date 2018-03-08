#!/usr/bin/env python3

from ev3dev.ev3 import *

# Sensor de color
cS = ColorSensor()
cS.mode = 'COL-REFLECT'

# Sensor de proximidad
iS = InfraredSensor() 
iS.mode = 'IR-PROX'

mA = largeMotor('outB')
mB = largeMotor('outC')

if iS.value()<10:
    Sound.speak('Nigga, Im the best!')




#negro 4
#azul 11
#cafe 30
#rojo 57

