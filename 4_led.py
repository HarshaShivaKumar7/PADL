import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ldr_pin = 7  
red_led_pin = 11 
green_led_pin = 13 
delay_time = 0.1

GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.output(red_led_pin, False)
GPIO.output(green_led_pin, False)

def read_ldr(ldr_pin):
    count = 0
    GPIO.setup(ldr_pin, GPIO.OUT)
    GPIO.output(ldr_pin, False)
    time.sleep(delay_time)
    GPIO.setup(ldr_pin, GPIO.IN)
    while (GPIO.input(ldr_pin) == 0):
        count += 1
    return count

try:
    while True:
        ldr_value = read_ldr(ldr_pin)
        print("LDR Value:", ldr_value)
        if ldr_value > 10000:
            print("Light is dim")
            GPIO.output(red_led_pin, True)
            GPIO.output(green_led_pin, False)
        else:
            print("Light is bright")
            GPIO.output(red_led_pin, False)
            GPIO.output(green_led_pin, True)
        time.sleep(1) 

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
