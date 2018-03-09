#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

#sensors
infra_s = InfraredSensor()
assert infra_s.connected, "Conecte un solo sensor de infrarrojos a cualquier puerto de sensor"

color_s = ColorSensor()
assert color_s.connected, "Conecte un sensor de color a cualquier puerto"

#modes
infra_s.mode = 'IR-PROX'
color_s = 'COL-REFLECT'

#vars
button = Button()
distance = infra_s.value()

while button.any():
    print(color_s.value())
    sleep(0.5)

'''
if distance < 60:
    Leds.set_color(Leds.LEFT, Leds.RED)
else:
    Leds.set_color(Leds.LEFT, Leds.GREEN)
'''

#enciende el led izquierdo en verde antes de acabar
Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)
