#!/usr/bin/env python3
from ev3dev.ev3 import *

btn = Button() #Usará cualquier boton para detener el script

#Comprobar si el sensor infrarojo está conectado
ir = InfraredSensor()
assert ir.connected, "El sensor funciona correctamente"

#Conecta los motores grandes a los puertos B y C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=50)
mC.run_forever(speed_sp=50)