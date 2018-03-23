#!/usr/bin/env python3
from ev3dev.ev3 import* 
from time import sleep
from random import randint, uniform,random

btn = Button()#Boton para que se detenga el programa

#Sensor de color
cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode = 'COL-COLOR'

#Sensor de proximidad
ir = InfraredSensor()
assert ir.connected, "Connect an IR sensor to any sensor port"
ir.mode = 'IR-PROX'

#Iniciar Motores
mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=150)
mC.run_forever(speed_sp=150)

#Inicialización de variables
distance = ir.value();
count = 0 #Contador de basura
vuelta = 0 # 0=derecha; 1=izquierda

while not btn.any():
	#Proximidad
	if distance < 20:
		mB.stop()
		mC.stop()
		Sound.speak('Get out of my way!')
		sleep(3)
		mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
		mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
		mB.run_timed(time_sp=3000, speed_sp=500)
		mC.run_timed(time_sp=3000, speed_sp=500)
		mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  
		mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
		mB.wait_while('running')
		mC.wait_while('running')

	#Si se encuentra con NEGRO
	elif cl.value() == 1:
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
	#Si se encuentra con café
	elif cl.value() == 7:
		mB.run_forever(speed_sp=400)
		mC.run_forever(speed_sp=400)
	#Si se encuentra con AZUL 
	elif cl.value() == 2:
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

	#Si encuentra ROJO
	elif cl.value() == 5:
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

mB.stop(stop_action='brake')
mC.stop(stop_action='brake')