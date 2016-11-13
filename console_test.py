#!/usr/bin/python

import RPi.GPIO as GPIO
import time

controls = {
    'Power-LED': ({
        'switch': 0,
        'led': 13,
        'updown': 0,
        'state': 0
    }),
    'Switch 1': ({
        'switch': 12,
        'led': 19,
        'updown': GPIO.PUD_UP,
        'state': 0
    }),
    'Switch 2': ({
        'switch': 16,
        'led': 26,
        'updown': GPIO.PUD_UP,
        'state': 0
    }),
    'Switch 3': ({
        'switch': 20,
        'led': 5,
        'updown': GPIO.PUD_UP,
        'state': 0
    }),
    'Switch 4': ({
        'switch': 21,
        'led': 6,
        'updown': GPIO.PUD_UP,
        'state': 0
    }),
    'Kill-Switch': ({
        'switch': 24,
        'led': 0,
        'updown': GPIO.PUD_DOWN,
        'state': 0
    }),
    'Launch-Button': ({
        'switch': 25,
        'led': 0,
        'updown': GPIO.PUD_UP,
        'state': 0
    })
}


def setup():
    GPIO.setmode(GPIO.BCM)

    for x in controls:
        init_control = controls[x]
        if init_control['led'] > 0:
            GPIO.setup(init_control['led'], GPIO.OUT, initial=0)
            print "Setup LED " + str(init_control)
        if init_control['switch'] > 0:
            GPIO.setup(init_control['switch'], GPIO.IN, pull_up_down=init_control['updown'])
            print "Setup Switch " + str(init_control)


def switch(gpio, state):
    print "Switch " + str(gpio) + " to " + str(state)
    if state == 'on':
        GPIO.output(gpio, GPIO.HIGH)
    else:
        GPIO.output(gpio, GPIO.LOW)


def ready():
    print "System ready..."
    power_led = controls['Power-LED']
    switch(power_led['led'], 'on')


def launch_control():
    while 1:
        for i in controls:
            control = controls[i]
            if control['switch'] > 0:
                if GPIO.input(control['switch']) == GPIO.LOW:
                    if control['led'] > 0:
                        switch(control['led'], 'on')
                else:
                    if control['led'] > 0:
                        switch(control['led'], 'off')

        time.sleep(1)


def write_leds():
    for i in controls:
        control = controls[i]
        if control['led'] > 0:
            if control['state'] == 1:
                switch(control['led'], 'on')
            else:
                switch(control['led'], 'off')


def read_switches():
    for i in controls:
        control = controls[i]
        if control['switch'] > 0:
            state = GPIO.input(control['switch'])
            if control['updown'] == GPIO.PUD_UP:
                control['state'] = int(not state)
            else:
                control['state'] = int(state)

            print "Control " + str(control) + " to state: " + str(state)

setup()
ready()

try:
    while 1:
        read_switches()
        write_leds()

        time.sleep(.3)

except KeyboardInterrupt:
    GPIO.cleanup()
