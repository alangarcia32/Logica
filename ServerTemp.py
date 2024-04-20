# se usa Remote Data Exchange entre el raspberry pi y una PC
# se va usar el raspberry como un servidor y la pc como el cliente

import socket # van a utilizar para comunicarse
from time import sleep
import time
import RPi.GPIO as GPIO
import dht11
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

bufferSize = 1024
ServerPort = 2222
ServerIP = '192.168.1.175'

# este metodo es de los faciles
RPIServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sensor de temperatura y humedad

dhtPin = 17

DHT = dht11.DHT11(dhtPin)

trigPin = 23
echoPin = 24

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

RPIServer.bind((ServerIP, ServerPort))
print ('\nEl servidor esta esperando. . .')

try:
    while True:
        cmd, address = RPIServer.recvfrom(bufferSize)
        cmd = cmd.decode('utf-8')
        print (cmd)
        
        GPIO.output(trigPin, 0)
        time.sleep(0.00001)
        GPIO.output(trigPin, 1)
        time.sleep(10E-6)
        GPIO.output(trigPin, 0)

        while GPIO.input(echoPin) == 0:
            pass
        echoStartTime = time.time()

        while GPIO.input(echoPin) == 1:
            pass
        echoStopTime = time.time()

        echoTravelTime = echoStopTime - echoStartTime
        distance = echoTravelTime * 34300 / 2
        print (distance)
        time.sleep(1)

        if cmd == 'get_data':
            print ('\nClient Address: ', address[0])
            result = DHT.read()
            data = str(result.temperature) + ':' + str(result.humidity) + ':' + str(round(distance, 2))
            RPIServer.sendto(data.encode('utf-8'), address)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print ('\nGPIO has been cleaned')

