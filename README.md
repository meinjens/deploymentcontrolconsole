# Deployment Control Console

Console to control deployments

## Testing tool for console

Launch test tool:

    sudo python console_test.py
    
Configuration of GPIOs in controls dict:

    controls = {
        'Power-LED': ({
            'switch': 0,
            'led': 13,
            'updown': 0,
            'state': 0
        })
    }

|Key|Description|    
|---|---|
|switch|GPIO input to query a switch|
|led|GPIO output to control a LED|
|updown|Using Pull down (GPIO.PUD_DOWN) or pull up (GPIO.PUD_UP) for querying the state of a switch|
|state|Store actual state|

