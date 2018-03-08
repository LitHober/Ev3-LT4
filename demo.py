#!/usr/bin/env python3

'''
    source name: demo.py

    description:
    Lanza 2 hilos, un hilo de movimiento y un hilo de sentimiento.
     El subproceso move mueve el bot hacia adelante hasta que el hilo
     de feeldetecta un obstáculo.
     Luego, el hilo de movimiento hace que el bot se mueva en círculo
     hasta que el hilo de tacto detecta un toque en el sensor táctil.


'''

import sys
import time
import threading
import signal

from ev3dev import ev3

def movimiento(done):
    left_m = ev3.LargeMotor('outB'); assert left_m.connected
    right_m = ev3.LargeMotor('outC'); assert right_m.connected

    color_s = ev3.ColorSensor(); assert color_s.connected
    color_s.mode = 'COL-AMBIENT'

    speed = 250

    left_m.run_forever(speed_sp = speed)
    right_m.run_forever(speed_sp = speed)

    while not done.is_set():
        time.sleep(1)

    #detener ambos motores
    left_m.stop(stop_action = 'brake')
    right_m.stop(stop_action = 'brake')
    left_m.wait_while('running')
    right_m.wait_while('running')

    #correr en circulo
    done.clear()
    left_m.run_forever(speed_sp = speed)

    while not done.is_set():
        time.sleep(1)

    left_m.stop(stop_action = 'brake')
    left_m.wait_while('running')


def tacto(done):
    infra = ev3.InfraredSensor(); assert infra.connected
    touch = ev3.TouchSensor(); assert touch.connected

    screen = ev3.Screen()
    sound = ev3.Sound()

    screen.draw.text((60,40), 'Caminando')
    screen.update()

    while infra.proximity > 30:
        if done.is_set():
            break
        time.sleep(0.1)

    done.set() #lo detiene de su locura haha

    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)

    screen.clear()
    screen.draw.text((60,20), 'There is something is front of me')
    screen.update()

    while not touch_s.is_pressed:
        sound.speak("Where should i go next?").wait()
        time.sleep(0.5)

    done.set() #lo detiene de su locura haha

# El evento 'done' se usará para indicar que los hilos se detengan
done = threading.Event()

#we also neet to catch SIGINT (keyboard interrupt) and SIGTERM (termination signal from brickman) and exit gracefully
def signal_handler(signal, frame):
    done.set()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

#now that we have the worker functions defined, lets run those in separate threads
move_thread = threading.Thread(target= move, args=(done, ))
feel_thread = threading.Thread(target= move, args=(done, ))

move_thread.start()
feel_thread.start()

#the main thread will wait for the 'back' button to be pressed. when that
#happens, it will signal the worker threads to stop and wait for their completion
btn = ev3.Button()
while not btn.backspace and not done.is_set():
    time.sleep(1)

done.set()
move_thread.join()
feel_thread.join()

ev3.Sound.speak('Fareell and good bye')
ev3.Leds.all_off()
