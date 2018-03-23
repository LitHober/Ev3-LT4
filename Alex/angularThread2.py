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

def Blue():
    mB.run_forever(speed_sp=150)
    mC.run_forever(speed_sp=150)

    if color_value == 2:

        if vuelta == 0:
            num = randint(1, 3)

            #angulo 45°
            if num == 1:
                Sound.speak('I hate water')
                mB.run_to_rel_pos(position_sp=200, speed_sp=200, stop_action="brake")
                mC.run_to_rel_pos(position_sp=-200, speed_sp=200, stop_action="brake")
                time.sleep(1)
                mB.run_to_rel_pos(position_sp=250, speed_sp=200, stop_action="brake")
                mC.run_to_rel_pos(position_sp=-250, speed_sp=200, stop_action="brake")
                mB.wait_while('running')
                mC.wait_while('running')

                if vuelta == 1:
                    vuelta = 0
                elif vuelta == 0:
                    vuelta = 1

            # angulo 90°
            elif num == 2:
                Sound.speak('I hate water')
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

            # anuglo 120 °
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

# asignación de hilo
hilo_black = threading.Thread(name = 'Black', target = Black)
hilo_azul = threading.Thread(name = 'Blue', target = Blue)

# corre el hilo
hilo_black.start()
hilo_azul.start()
