#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from threading import Thread

#sensors & motors
infra_s = InfraredSensor()
color_s = ColorSensor()

#motor_B = LargeMotor('outB')
#motor_C = LargeMotor('outC')

#modes
infra_s.mode = 'IR-PROX'
color_s.mode = 'COL-COLOR'

#vars
distance = infra_s.value()

#funciones
def funcion1():
    mB = LargeMotor('outB')
    mC = LargeMotor('outC')

    mB.run_forever(speed = 900)
    sleep(5)
    mC.stop(stop_action = "hold")
    sleep(5)

hilo = Thread(target = funcion1)
hilo = start()
#def funcion2():
