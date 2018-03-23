#!/usr/bin/env python 3

from ev3dev.ev3 import *
from time import sleep
from random import randint, uniform, random
import threading

btn = Button()
infra = InfraredSensor()
color = ColorSensor()
mB = LargeMotor('outB')
mC = LargeMotor('outC')

color.mode = 'COL-COLOR'
infra.mode = 'IR-PROX'

distance = infra.value()
color_value = color.value()
count = 0
vuelta = 0

def Black():
    mB.run_forever(speed_sp=150)
    mC.run_forever(speed_sp=150)

    if color_value == 1:
        Sound.speak('Black')
        count += 1
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

    mB.stop(stop_action='brake')
    mC.stop(stop_action='brake')

def Brown():
    mB.run_forever(speed_sp=150)
    mC.run_forever(speed_sp=150)

        if color_value == 7:
            mB.run_forever(speed_sp=400)
            mC.run_forever(speed_sp=400)

hilo_Black = threading.Thread(name='Black', target=Black)
hilo_Brown = threading.Thread(name='Brown', target=Brown)

hilo_Black.start()
hilo_Brown.start()
