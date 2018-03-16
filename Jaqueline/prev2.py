#!/usr/bin/env python3 
from ev3dev.ev3 import * 

import threading
import logging 

def R_corr();
	boton = Button() 

	mB = LargeMotor('outB')
	mC = LargeMotor('outC')

while not boton.any():
	mB = run_forever(speed_sp=50)
	mC = run_forever(speed_sp=50)

hilo = threading.Thread(target = R_corr)
hilo.start()

