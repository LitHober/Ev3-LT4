#!/usr/bin/env python3
from ev3dev.ev3 import *

btn = Button() #Usará cualquier boton para detener el script

cl = ColorSensor() #Conectara el sensor de color
cl.mode='COL-COLOR'

#Conecta los motores grandes a los puertos B y C
mB = LargeMotor('outB')
mC = LargeMotor('outC')
direccion = 0

while not btn.any():    #Se sale del loop cuando presionas cualquier boton
	
	if direccion == 0:
		mB.run_timed(time_sp=3000, speed_sp=500)
		mC.run_timed(time_sp=3000, speed_sp=500)
		mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
		mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
		if direccion == 0:
			direccion = 1
		else:
			direccion = 0
			
	elif direccion == 1: 
      		mB.run_timed(time_sp=3000, speed_sp=500)
		mC.run_timed(time_sp=3000, speed_sp=500)
		mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
		mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
		if direccion == 0:
			direccion = 1
		else:
			direccion = 0
			
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
