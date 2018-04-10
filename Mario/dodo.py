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

#Arranca los motores
mB.run_forever(speed_sp=700)
mC.run_forever(speed_sp=700)

#Inicialización de variables

dc = ir.value();
count = 0 #Contador de basura
vuelta = 0 # 0=derecha; 1=izquierda (usado cuando se encuentra el color azul)
vp = 0 #Variable para elgir la vuelta del sensor de proximidad
vn = 0 #Variable para elgir la vuelta del sensor de color cuando encuentra negro

while not btn.any():#Mientras no se apriete ningun boton, se ejecutan las condiciones dentro del while
	#Proximidad
	if ir.value() < 20:#Si el sensor reconoce un objeto a menos de 20 unidades 
		if vp == 0:		#Si la vaiable es 0, gira a la derecha
			mB.stop()	#Detiene los motores
			mC.stop()	#Detiene los motores
			Sound.speak('Sorry') 
			mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
			mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
			sleep(1)
			mB.run_to_rel_pos(position_sp=500, speed_sp=300, stop_action="brake")	#Avanza 500 el motor B
			mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake")	#Retrocede -500 el motor C
			vp = 1  	#Cambia la variable para cambiar la vuelta la proxima vez
		elif vp == 1:	#Si la vaiable es 1, gira a la izquierda
			mB.stop()	#Detiene el motor B
			mC.stop()	#Detiene el motor C
			Sound.speak('Sorry')
			mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
			mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
			sleep(1)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake")  #Retrocede -500 el motor B
			mC.run_to_rel_pos(position_sp=500, speed_sp=300, stop_action="brake")	#Avanza 500 el motor C
			vp = 0		#Cambia la variable para cambiar la vuelta la proxima vez
		
	#Si se encuentra con NEGRO
	elif cl.value() == 1:
		if vn == 0: #Si la vaiable es 0, gira a la derecha
			Sound.speak('black')
			count += 1 #Agrega al contador una basura
			mB.stop()	#Detiene el motor B
			mC.stop()	#Detiene el motor C
			sleep(3)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  #Retrocede -500
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")	#Retrocede -500
			mB.run_timed(time_sp=3000, speed_sp=500)
			mC.run_timed(time_sp=3000, speed_sp=500)
			mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")  	#Avanza 500 el motor B
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")	#Retrocede -500 el motor C
			mB.wait_while('running')
			mC.wait_while('running')
			vn = 1 		#Cambia la variable para cambiar la vuelta la proxima vez
		elif vn == 1:	#Si la vaiable es 1, gira a la izquierda
			Sound.speak('black')
			count += 1 #Agrega al contador una basura
			mB.stop() #Detiene el motor B
			mC.stop() #Detiene el motor C
			sleep(3)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  #Retrocede -500
			mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")	#Retrocede -500
			mB.run_timed(time_sp=3000, speed_sp=500)
			mC.run_timed(time_sp=3000, speed_sp=500)
			mB.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  #Retrocede -500 el motor B
			mC.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")	#Avanza 500 el motor C
			mB.wait_while('running')
			mC.wait_while('running')
			vn = 0 		#Cambia la variable para cambiar la vuelta la proxima vez
	#Si se encuentra con AZUL 
	elif cl.value() == 2:
		if vuelta == 0: 		#Si la vuelta es igual a 0 (gira a la derecha)
			num = randint(1,3)
			#Angulo de 45
			if num == 1:
				Sound.speak('Oh no, I hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				sleep(1)
				mB.run_to_rel_pos(position_sp=200, speed_sp=300, stop_action="brake")  #Avanza 200 el motor B
				mC.run_to_rel_pos(position_sp=-200, speed_sp=300, stop_action="brake") #Retrocede -200 el motor
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:			#Si la variable vuelta es 1, la cambia a 0 y viceversa 
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Oh no, I hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				sleep(1)
				mB.run_to_rel_pos(position_sp=600, speed_sp=300, stop_action="brake")  #Avanza 600 el motor B
				mC.run_to_rel_pos(position_sp=-600, speed_sp=300, stop_action="brake") #Retrocede -600 el motor C
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:			#Si la variable vuelta es 1, la cambia a 0 y viceversa
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Oh no, I hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				sleep(1)
				mB.run_to_rel_pos(position_sp=800, speed_sp=300, stop_action="brake")  #Avanza 800 el motor B
				mC.run_to_rel_pos(position_sp=-800, speed_sp=300, stop_action="brake") #Retrocede -800 el motor C
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:			#Si la variable vuelta es 1, la cambia a 0 y viceversa
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			else:
				mB.run_forever(speed_sp=600)
				mC.run_forever(speed_sp=600)

		elif vuelta == 1:		#Si la vuelta es igual a 0 (gira a la izquierda)
			num = randint(1,3)
			if num == 1:
				Sound.speak('Oh no, i hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				sleep(1)
				mB.run_to_rel_pos(position_sp=-200, speed_sp=300, stop_action="brake")  #Retrocede -200 el motor B
				mC.run_to_rel_pos(position_sp=200, speed_sp=300, stop_action="brake") 	#Avanza 200 el motor C
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:			#Si la variable vuelta es 1, la cambia a 0 y viceversa
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 90
			elif num == 2:
				Sound.speak('Oh no, I hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				sleep(1)
				mB.run_to_rel_pos(position_sp=-600, speed_sp=300, stop_action="brake")  #Retrocede -600 el motor B
				mC.run_to_rel_pos(position_sp=600, speed_sp=300, stop_action="brake") 	#Avanza 600 el motor C
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:			#Si la variable vuelta es 1, la cambia a 0 y viceversa
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			#Ángulo de 120
			elif num == 3:
				Sound.speak('Oh no, I hate water')
				mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
				sleep(1)
				mB.run_to_rel_pos(position_sp=-800, speed_sp=300, stop_action="brake")  #Retrocede -800 el motor B
				mC.run_to_rel_pos(position_sp=800, speed_sp=300, stop_action="brake") 	#Avanza 800 el motor C
				mB.wait_while('running')
				mC.wait_while('running')
				if vuelta == 1:			#Si la variable vuelta es 1, la cambia a 0 y viceversa
					vuelta = 0
				elif vuelta == 0:
					vuelta = 1
			else:
				mB.run_forever(speed_sp=700)	#Permanece avanzando a una velocidad de 700
				mC.run_forever(speed_sp=700)
		else:
			mB.run_forever(speed_sp=700)		#Permanece avanzando a una velocidad de 700
			mC.run_forever(speed_sp=700)

	#Si encuentra ROJO
	elif cl.value() == 5:
		mB.stop()
		mC.stop()
		while count != 0:
			Sound.beep() #Hace un beep cada que el contador de basura disminuye
			count -= 1 #Deposita una basura
			sleep(1)
		mB.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
		mC.run_to_rel_pos(position_sp=-500, speed_sp=300, stop_action="brake") #Retrocede -500
		sleep(1)
		mB.run_to_rel_pos(position_sp=600, speed_sp=300, stop_action="brake")  #Avanza 600 el motor B
		mC.run_to_rel_pos(position_sp=-600, speed_sp=300, stop_action="brake") #Retrocede -600 el motor C
		mB.wait_while('running')
		mC.wait_while('running')
		mB.run_forever(speed_sp=700)	#Avanza el motor B
		mC.run_forever(speed_sp=700)	#Avanza el motor C

	else:
		mB.run_forever(speed_sp=700)
		mC.run_forever(speed_sp=700)

mB.stop(stop_action='brake')
mC.stop(stop_action='brake')