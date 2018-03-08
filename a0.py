#!/usr/bin/env python3

from ev3dev.ev3 import *

infra_s = InfraredSensor()
assert infra_s.connected, "Conecte un solo sensor de infrarrojos a cualquier puerto de sensor"

color_s = ColorSensor()
assert color_s.connected, "Conecte un sensor de color a cualquier puerto"

infra_s.mode = 'IR-PROX'

distance = infra_s.value()

if distance < 60:
    Leds.set_color(Leds.LEFT, Leds.RED)
else:
    Leds.set_color(Leds.LEFT, Leds.GREEN)

Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)
