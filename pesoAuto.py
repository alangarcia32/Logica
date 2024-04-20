# calibra la pesa automaticamente usando memoria

import os
from time import sleep
import RPi.GPIO as GPIO
from hx711 import HX711
GPIO.setmode(GPIO.BCM)

dataPin = 17
clkPin = 27

hx711 = HX711(dataPin, clkPin)

knownWeight = 1000  # cambiarlo por otro y debe ser en gramos

calibrationFile = "calibrationFactor.txt" # es el archivo en donde se va guardar el peso

# Function to load calibration factor from file
def loadCalibrationFactor():
    # Check if calibration file exists
    if os.path.exists(calibrationFile):
        # If file exists, read calibration factor from it
        with open(calibrationFile, "r") as file:
            return float(file.read().strip())
    else:
        # If file does not exist, return None
        return None

# Function to save calibration factor to file
def saveCalibrationFactor(calibrationFactor):
    # Save calibration factor to file
    with open(calibrationFile, "w") as file:
        file.write(str(calibrationFactor))

# Function to calibrate the scale
def calibrateScale():
    print("Calibrando pesa . . .")

    # Read raw data from the sensor
    rawWeight = hx711.get_raw_data_mean()

    # Calculate calibration factor
    calibrationFactor = knownWeight / rawWeight

    print("Calibracion exitosa")

    # Save calibration factor in memory
    saveCalibrationFactor(calibrationFactor)

    return calibrationFactor

# Main function
def main():
    # Load calibration factor from file
    calibrationFactor = loadCalibrationFactor()

    # If calibration factor is not available, calibrate the scale
    if calibrationFactor is None:
        calibrationFactor = calibrateScale()

    # Set the scale ratio
    hx711.set_scale_ratio(calibrationFactor)

    try:
        # Main loop to continuously read and display weight
        while True:
            # Read raw data from the sensor
            rawDataList = [hx711.get_raw_data_mean() for _ in range(20)]
            
            rawWeightMean = sum(rawDataList) / len(rawDataFactor)

            # Apply calibration factor to get calibrated weight
            calibratedWeight = rawWeight * calibrationFactor

            print("Weight:", calibratedWeight, "grams")
            sleep(1)
            
    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
        print ('GPIO has been cleaned')

# Check if the script is being run directly
if __name__ == "__main__":
    main()