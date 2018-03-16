#!/usr/bin/env python3

from ev3dev.ev3 import *
import threading
import time

#sensors & motors
infra_s = InfraredSensor()
color_s = ColorSensor()
mB = LargeMotor('outB')
mC = LargeMotor('outC')


#modes
infra_s.mode = 'IR-PROX'
color_s.mode = 'COL-COLOR'

#vars
distance = infra_s.value()

#funciones
def funcion1():
    mB.run_forever(speed_sp = 900)
    mC.run_forever(speed_sp = 900)
    time.sleep(5)
    mB.stop(stop_action = "hold")
    mC.stop(stop_action = "hold")
    time.sleep(5)
    Sound.beep()

def funcion2():
    for i in range(5):
        Sound.beep()
    

hilo1 = threading.Thread( name = 'funcion1', target = funcion1)
hilo2 = threading.Thread( name = 'funcion2', target = funcion2)

hilo1.start()
hilo2.start()

