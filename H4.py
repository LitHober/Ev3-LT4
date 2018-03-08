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

mA.run_forever(speed_sp=100)
mB.run_forever(speed_sp=100)

if iS.value()<20:
    mA.run_forever(speed_sp=-100)
    mB.run_forever(speed_sp=-100)
    


#negro 4
#azul 11
#cafe 30
#rojo 57

