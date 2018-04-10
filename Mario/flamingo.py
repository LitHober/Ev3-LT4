#!/usr/bin/env python3
from ev3dev.ev3 import* 
from time import sleep
from random import randint, uniform,random

btn = Button()#Boton para que se detenga el programa

#Sensor de color
cl = ColorSensor('in3')
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode = 'COL-COLOR'

#Sensor de proximidad
ir = InfraredSensor()
assert ir.connected, "Connect an IR sensor to any sensor port"
ir.mode = 'IR-PROX'

#Iniciar Motores
mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.run_forever(speed_sp=700)
mC.run_forever(speed_sp=700)

#Inicialización de variables
dc = ir.value();
count = 0 #Contador de basura
vuelta = 0 # 0=derecha; 1=izquierda
vp = 0
vn = 0

while not btn.any():
	#Proximidad
	if ir.value() < 20:
		if vp == 0:
			mB.stop()
			mC.stop()
			Sound.speak('Sorry')
			mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
			mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
			sleep(1)
			mB.run_to_rel_pos(position_sp=500, speed_sp=300, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake")
			vp = 1
		elif vp == 1:
			mB.stop()
			mC.stop()
			Sound.speak('Sorry')
			mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
			mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
			sleep(1)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=300, stop_action="brake")
			vp = 0
		
	#Si se encuentra con NEGRO
	elif cl.value() == 1:
		if vn == 0:
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
			vn = 1
		elif vn == 1:
			Sound.speak('black')
			count += 1 #Agrega al contador una basura
			mB.stop()
			mC.stop()
			sleep(3)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			mB.run_timed(time_sp=3000, speed_sp=500)
			mC.run_timed(time_sp=3000, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
			mB.wait_while('running')
			mC.wait_while('running')
			vn = 0
	#Si se encuentra con café
	elif cl.value() == 7:
		mB.run_forever(speed_sp=600)
		mC.run_forever(speed_sp=600)
	#Si se encuentra con AZUL 
	elif cl.value() == 2:
		if vuelta == 0:
			num = randint(1,3)
			#Angulo de 45
			if num == 1:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=200, speed_sp=300, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-200, speed_sp=300, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=600, speed_sp=300, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-600, speed_sp=300, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=800, speed_sp=300, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=-800, speed_sp=300, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			else:
				mB.run_forever(speed_sp=600)
				mC.run_forever(speed_sp=600)

		elif vuelta == 1:
			num = randint(1,3)
			if num == 1:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-200, speed_sp=300, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=200, speed_sp=300, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-600, speed_sp=300, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=600, speed_sp=300, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Fuck, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") 
				sleep(1)
				mB.run_to_rel_pos(position_sp=-800, speed_sp=300, stop_action="brake")  
				mC.run_to_rel_pos(position_sp=800, speed_sp=300, stop_action="brake") 
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			else:
				mB.run_forever(speed_sp=700)
				mC.run_forever(speed_sp=700)
		else:
			mB.run_forever(speed_sp=700)
			mC.run_forever(speed_sp=700)

	#Si encuentra ROJO
	elif cl.value() == 5:
		mB.stop()
		mC.stop()
		Sound.speak('red is a container')
		while count != 0:
			Sound.beep()
			count -= 1 #Deposita una basura
			sleep(1)
	else:
		mB.run_forever(speed_sp=700)
		mC.run_forever(speed_sp=700)

mB.stop(stop_action='brake')
mC.stop(stop_action='brake')