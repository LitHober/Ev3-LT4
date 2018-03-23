#!/usr/bin/env python3
from ev3dev.ev3 import* 
from time import sleep
from random import randint, uniform,random
import threading

btn = Button()#Boton para que se detenga el programa

#Sensor de color
cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode = 'COL-COLOR'

mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=150)
mC.run_forever(speed_sp=150)
count = 0 #Contador de basura
vuelta = 0 # 0=derecha; 1=izquierda

###########################################################################################
#Si se encuentra con negro
def black():
	if cl.value() == 1:
		Sound.speak('black')
		count += 1 #Agrega al contador una basura
		mB.stop()
		mC.stop()
		sleep(3)
		mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
		mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
		mB.run_timed(time_sp=3000, speed_sp=500)
		mC.run_timed(time_sp=3000, speed_sp=500)
		mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
		mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
		mB.wait_while('running')
		mC.wait_while('running')
###########################################################################################

#Si se encuentra con café
def brown():
	if cl.value() == 7:
		mB.run_forever(speed_sp=400)
		mC.run_forever(speed_sp=400)
###########################################################################################

#Si se encuentra con AZUL
def blue():
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
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=550, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-550, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=750, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-750, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			else:
				mB.run_forever(speed_sp=400)
				mC.run_forever(speed_sp=400)

		elif vuelta == 1:
			num = randint(1,3)
			if num == 1:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-250, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=250, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-550, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=550, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-750, speed_sp=200, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=750, speed_sp=200, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			else:
				mB.run_forever(speed_sp=400)
				mC.run_forever(speed_sp=400)
		else:
			mB.run_forever(speed_sp=400)
			mC.run_forever(speed_sp=400)

###########################################################################################
#Si encuentra ROJO
def red():
	if cl.value() == 5:
		Sound.speak('red is a container')
		mB.stop()
		mC.stop()
		while count != 0:
			count -= 1 #Deposita una basura
			Sound.beep()
		sleep(3)
	else:
		mB.run_forever(speed_sp=400)
		mC.run_forever(speed_sp=400)
###########################################################################################
#Asignación del hilo
hilo_black = threading.Thread(name = 'black', target = black)
hilo_brown = threading.Thread(name = 'brown', target = brown)
hilo_blue = threading.Thread(name = 'blue', target = blue)
hilo_red = threading.Thread(name = 'red', target = red)

###########################################################################################
#Correr hilos
hilo_brown.start()
hilo_black.start()
hilo_blue.start()
hilo_red.start()

mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
