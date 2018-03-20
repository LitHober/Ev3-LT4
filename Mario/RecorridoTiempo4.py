#!/usr/bin/env python3
from ev3dev.ev3 import *
from random import randint, uniform,random

btn = Button() #Usará cualquier boton para detener el script

cl = ColorSensor() #Conectara el sensor de color
cl.mode='COL-COLOR'

#Conecta los motores grandes a los puertos B y C
mB = LargeMotor('outB')
mC = LargeMotor('outC')
direccion = 0

while not btn.any():    #Se sale del loop cuando presionas cualquier boton
	
	mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
	mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")

	num = randint(5,9)

	if num == 5:
		if direccion == 0:
			mB.run_timed(time_sp=30, speed_sp=500)
			mC.run_timed(time_sp=30, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0  

		elif direccion == 1: 
			mB.run_timed(time_sp=30, speed_sp=500)
			mC.run_timed(time_sp=30, speed_sp=500)
			mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0

	if num == 6:
		if direccion == 0:
			mB.run_timed(time_sp=40, speed_sp=500)
			mC.run_timed(time_sp=40, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0  

		elif direccion == 1: 
			mB.run_timed(time_sp=40, speed_sp=500)
			mC.run_timed(time_sp=40, speed_sp=500)
			mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0

	if num == 7:
		if direccion == 0:
			mB.run_timed(time_sp=50, speed_sp=500)
			mC.run_timed(time_sp=50, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0  

		elif direccion == 1: 
			mB.run_timed(time_sp=50, speed_sp=500)
			mC.run_timed(time_sp=50, speed_sp=500)
			mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0

	if num == 8:
		if direccion == 0:
			mB.run_timed(time_sp=60, speed_sp=500)
			mC.run_timed(time_sp=60, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0  

		elif direccion == 1: 
			mB.run_timed(time_sp=60, speed_sp=500)
			mC.run_timed(time_sp=60, speed_sp=500)
			mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0

	if num == 9:
		if direccion == 0:
			mB.run_timed(time_sp=70, speed_sp=500)
			mC.run_timed(time_sp=70, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0  

		elif direccion == 1: 
			mB.run_timed(time_sp=70, speed_sp=500)
			mC.run_timed(time_sp=70, speed_sp=500)
			mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
			if direccion == 0:
				direccion = 1
			else:
				direccion = 0

mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
