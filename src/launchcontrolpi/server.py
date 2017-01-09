from flask import Flask, request, jsonify

from launchcontrolpi.hardware.led import GPIOLed

app = Flask(__name__)


leds = {
    1: GPIOLed('Power', False, 18),
    2: {
        'name': 'Switch 1',
        'state': False
    },
    3: {
        'name': 'Switch 2',
        'state': False
    },
    4: {
        'name': 'Switch 3',
        'state': False
    },
    5: {
        'name': 'Switch 4',
        'state': False
    }
}

switches = {
    1: {
        'name': 'Switch 1',
        'state': False
    },
    2: {
        'name': 'Switch 2',
        'state': False
    },
    3: {
        'name': 'Switch 3',
        'state': False
    },
    4: {
        'name': 'Switch 4',
        'state': False
    },
    5: {
        'name': 'Kill Switch',
        'state': False
    },
    6: {
        'name': 'Launch Switch',
        'state': False
    }
}


@app.route('/led/list')
def get_leds():
    return jsonify(leds)


@app.route('/led/<led_id>', methods=['GET', 'PUT'])
def is_led_on(led_id):
    if request.method == 'PUT':
        pass
    else:
        led = leds[int(led_id)]

        return jsonify(led)


@app.route('/switch/list')
def get_switches():
    return jsonify(switches)


@app.route('/switch/<switch_id>', methods=['GET'])
def is_switch_on(switch_id):
    switch = switches[int(switch_id)]

    return jsonify(switch)


if __name__ == "__main__":
    app.run()
