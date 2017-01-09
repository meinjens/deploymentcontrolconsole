import logging
from launchcontrolpi.hardware.hardware import AbstractHardware


try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.")


logging.basicConfig(level=logging.INFO)


class GPIOSwitch(AbstractHardware):
    pin = None
    logger = logging.getLogger(__name__)

    def __init__(self, name='undefined', state=False, pin=None):
        super(GPIOSwitch, self).__init__(name, state)
        self.pin = pin

        self.setup()

    def setup(self):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

        self.logger.debug('Setup hardware switch [pin %s]', self.pin)

    def cleanup(self):
        GPIO.cleanup(self.pin)

    def read_state(self):
        self.state = GPIO.input(self.pin)

        return self.state

    def write_state(self, state):
        self.logger.info('You cannot write a state to a hardware switch', self.pin)

        return self.state
