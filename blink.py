from time import sleep
import RPi.GPIO as GPIO
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
while (True):
     GPIO.output(13, False)
     sleep(1)
     GPIO.output(13, True)
     sleep(1)

     GPIO.output(15, False)
     sleep(1)
     GPIO.output(15, True)
     sleep(1)

     GPIO.output(16, False)
     sleep(1)
     GPIO.output(16, True)
     sleep(1)
     if KeyboardInterrupt:
          GPIO.output(13, False)
          GPIO.output(15, False)
          GPIO.cleanup()

	 
