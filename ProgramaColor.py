#!/usr/bin/env python3
from ev3dev.ev3 import *

btn = Button() #Usará cualquier boton para detener el script

cl = ColorSensor() #Conectara el sensor de color

#Pone el sensor de color en modo COL-REFLECT
#para medir la intensidad de la luz reflejada
cl.mode='COL-REFLECT'

#Conecta los motores grandes a los puertos B y C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while not btn.any():    #Se sale del loop cuando presionas cualquier boton
    if cl.value()<30:   #Reflejo debil sobre la linea negra
        #Media vuelta a la derecha
        mB.run_forever(speed_sp=50)
        mC.stop(stop_action='brake')
    else:   #Reflejo fuerte (>=30) sobre la superficie blanca
        #Media vuelta a la izquierda
        mB.stop(stop_action='brake')
        mC.run_forever(speed_sp=50)
      
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')