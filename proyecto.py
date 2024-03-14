from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Variables del dispensador de comida
buttonA = 3 # almacen
buttonB = 5 # tiempo
buttonC = 7 # plato
buttonD = 11 # aplicacion

# Variables del dispensador de agua
buttonE = 13 # almacen
buttonF = 15 # plato

# LEDS del dispensador de comida
salidaComida = 8
notificacionComida = 10
nadaComida = 12

# LEDS del dispensador de comida
salidaAgua = 16
notificacionAgua = 18
nadaAgua = 19

# Declaracion de las variables del dispensador de comida
GPIO.setup(buttonA, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonB, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonC, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonD, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(salidaComida, GPIO.OUT)
GPIO.setup(notificacionComida, GPIO.OUT)
GPIO.setup(nadaComida, GPIO.OUT)

# Declaracion de las variables del dispensador de agua
GPIO.setup(buttonE, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonF, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(salidaAgua, GPIO.OUT)
GPIO.setup(notificacionAgua, GPIO.OUT)
GPIO.setup(nadaAgua, GPIO.OUT)

try:
	while True:
		buttonAState = GPIO.input(buttonA)
		buttonBState = GPIO.input(buttonB)
		buttonCState = GPIO.input(buttonC)
		buttonDState = GPIO.input(buttonD)
		buttonEState = GPIO.input(buttonE)
		buttonFState = GPIO.input(buttonF)

		print ('\nA: ', buttonAState)
		print ('B: ', buttonBState)
		print ('C: ', buttonCState)
		print ('D: ', buttonDState)
		print ('E: ', buttonEState)
		print ('F: ', buttonFState)

		if buttonAState == 0:
			if buttonBState == 0:
				GPIO.output(nadaComida, 1)
				if buttonEState == 0:
					if buttonFState == 0:
						GPIO.output(nadaAgua, 1)
					elif buttonFState == 1:
						GPIO.output(salidaAgua, 1)
				elif buttonEState == 1:
					GPIO.output(notificacionAgua, 1)
			elif buttonBState == 1:
				if buttonCState == 0:
					if buttonDState == 0:
						GPIO.output(nadaComida, 1)
						if buttonEState == 0:
							if buttonFState == 0:
								GPIO.output(nadaAgua, 1)
							elif buttonFState == 1:
								GPIO.output(salidaAgua, 1)
						elif buttonEState == 1:
							GPIO.output(notificacionAgua, 1)
					elif buttonDState == 1:
						GPIO.output(salidaComida, 1)
						if buttonEState == 0:
							if buttonFState == 0:
								GPIO.output(nadaAgua, 1)
							elif buttonFState == 1:
								GPIO.output(salidaAgua, 1)
						elif buttonEState == 1:
							GPIO.output(notificacionAgua, 1)
				elif buttonCState == 1:
					GPIO.output(salidaComida, 1)
					if buttonEState == 0:
						if buttonFState == 0:
							GPIO.output(nadaAgua, 1)
						elif buttonFState == 1:
							GPIO.output(salidaAgua, 1)
					elif buttonEState == 1:
						GPIO.output(notificacionAgua, 1)
		elif buttonAState == 1:
			GPIO.output(notificacionComida, 1)
			if buttonEState == 0:
				if buttonFState == 0:
					GPIO.output(nadaAgua, 1)
				elif buttonFState == 1:
					GPIO.output(salidaAgua, 1)
			elif buttonEState == 1:
				GPIO.output(notificacionAgua, 1)

		sleep(0.8)
		GPIO.output(nadaComida, 0)
		GPIO.output(notificacionComida, 0)
		GPIO.output(salidaComida, 0)
		GPIO.output(nadaAgua, 0)
		GPIO.output(notificacionAgua, 0)
		GPIO.output(salidaAgua, 0)

except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
	print ('\nGPIO has been cleaned')
