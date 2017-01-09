import logging
from launchcontrolpi.hardware.hardware import AbstractHardware


try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.")


logging.basicConfig(level=logging.INFO)


class GPIOLed(AbstractHardware):
    pin = None
    logger = logging.getLogger(__name__)

    def __init__(self, name='undefined', state=False, pin=None):
        super(GPIOLed, self).__init__(name, state)
        self.pin = pin

        self.setup()

    def setup(self):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        self.logger.debug('Setup hardware switch [pin %s]', self.pin)

    def cleanup(self):
        GPIO.cleanup(self.pin)

    def read_state(self):
        self.state = GPIO.input(self.pin)

        return self.state

    def write_state(self, state):
        if state == 1:
            GPIO.output(self.pin, GPIO.HIGH)
            self.state = 1

            self.logger.info('Turn LED [pin %s] on.', self.pin)
        else:
            GPIO.output(self.pin, GPIO.LOW)
            self.state = 0

            self.logger.info('Turn LED [pin %s] off.', self.pin)

        return self.state
