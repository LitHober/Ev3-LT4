#!/usr/bin/env python3

from ev3dev.ev3 import* 
from time import sleep
from random import randint, uniform,random

btn = Button()#Boton para que se detenga el programa

#Sensor de color
cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode = 'COL-COLOR'

mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=150)
mC.run_forever(speed_sp=150)
vuelta = 0 # 0=derecha; 1=izquierda

while not btn.any():
	if cl.value() == 2:
		if vuelta == 0:
			num = randint(1,3)
			#Angulo de 45
			if num == 1:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=250, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-250, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				#vuelta = 1
				mB.run_forever(speed_sp=150)
				mC.run_forever(speed_sp=150)
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=585, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-585, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				#vuelta = 1
				mB.run_forever(speed_sp=150)
				mC.run_forever(speed_sp=150)
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=700, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-700, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				#vuelta = 1
				mB.run_forever(speed_sp=150)
				mC.run_forever(speed_sp=150)

		'''else vuelta == 1:
			if num == 1:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-685, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=685, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				vuelta = 1
				mB.run_forever(speed_sp=150)
				mC.run_forever(speed_sp=150)
			#Ángulo de 90
			elif num == 2:

			#Ángulo de 120
			elif num == 3:'''
				
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')