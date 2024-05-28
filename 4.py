import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
delayt = .1 
value = 0 # this variable will be used to store the ldr value
ldr = 7 #ldr is connected with pin number 7
led = 11
led_2 = 13#led is connected with pin number 11
GPIO.setup(led, GPIO.OUT)# as led is an output device so that’s why we set it to output.
GPIO.setup(led_2, GPIO.OUT)
GPIO.output(led, False) # keep led off by default
GPIO.output(led_2, False)
def rc_time (ldr):
    count = 0

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayt)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1

    return count


#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print("Ldr Value:")
        value = rc_time(ldr)
        print(value)
        if ( value <= 10000 ):
                print("Lights are ON")
                GPIO.output(led_2, False)
                GPIO.output(led, True)
        else:
                print("Lights are OFF")
                GPIO.output(led, False)
                GPIO.output(led_2, True)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()