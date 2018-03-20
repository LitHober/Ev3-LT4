#!/usr/bin/env python3
from ev3dev.ev3 import* 
from time import sleep
from random import randint, uniform,random
import threading
import time

btn = Button()#Boton para que se detenga el programa

#Sensor de color
cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode = 'COL-COLOR'

def funcion1():
mB = LargeMotor('outB')
mC = LargeMotor('outC')
mB.run_forever(speed_sp=150)
mC.run_forever(speed_sp=150)
count = 0 #Contador de basura
vuelta = 0 # 0=derecha; 1=izquierda

while not btn.any():
	if cl.value() == 1:
		Sound.speak('black')
		mB.stop()
		mC.stop()
		sleep(3)
		count += 1 #Agrega al contador una basura
		mB.run_forever(speed_sp=400)
		mC.run_forever(speed_sp=400)

hilo1 = threading.Thread( name = 'funcion1', target = funcion1)

hilo1.start()