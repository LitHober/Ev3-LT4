#!/usr/bin/env python 3

from ev3dev.ev3 import *
import threading
import time

#sensors & motors
infra = InfraredSensor()
color = ColorSensor()
mB = LargeMotor('outB')
mC = LargeMotor('outC')

#modes
color.mode = 'COL-COLOR'
infra.mode = 'IR-PROX'

#variables
distance = infra.value()
color_value = color.value()
#counters
count = 0 #contador de basura
vuelta = 0 #0->derecha 1->izquierda

#funciones
def Black():
    mB.run_forever(speed_sp=150)
    mC.run_forever(speed_sp=150)

    if color_value ==1:
        Sound.speak('black')
        count += 1
        mB.stop()
        mC.stop()
        time.sleep(3)
        mB.run_to_rel_pos(position_sp = 500, speed_sp = 200, stop_action = "brake")
        mC.run_to_rel_pos(position_sp = -500, speed_sp = 200, stop_action = "brake")
        mB.run_timed(time_sp=3000, speed_sp=500)
        mC.run_timed(time_sp=3000, speed_sp=500)
        mB.run_to_rel_pos(position_sp=500, speed_sp=200, stop_action="brake")
        mC.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")
        mB.wait_while('running')
        mC.wait_while('running')

    mB.stop(stop_action='brake')
    mC.stop(stop_action='brake')

# asignación de hilo
hilo_black = threading.Thread(name = 'Black', target = Black)

# corre el hilo
hilo_black.start()
