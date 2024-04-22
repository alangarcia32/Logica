# realiza un evento con un horario

import RPi.GPIO as GPIO
import datetime
import time
GPIO.setmode(GPIO.BCM)

led = 13
GPIO.setup(led, GPIO.OUT)

def lightOn():
    GPIO.output(led, GPIO.HIGH)
    print("Light turned on")

def lightOff():
    GPIO.output(led, GPIO.LOW)
    print("Light turned off")

# Desired time to turn on the light (24-hour format)
hora1 = 11
minuto1 = 43

hora2 = 20
minuto2 = 35

try:
    while True:
        current_time = datetime.datetime.now()
        
        # Check if the current time matches the desired time to turn on the light
        if current_time.hour == hora1 and current_time.minute == minuto1 or current_time.hour == hora2 and current_time.minute == minuto2:
            lightOn()
            # Sleep to avoid turning on the light repeatedly
            time.sleep(60)
            
            lightOff()
        
        # Sleep for a short duration to avoid high CPU usage
        time.sleep(10)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print ('\nGPIO has been cleaned')