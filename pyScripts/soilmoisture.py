import RPi.GPIO as GPIO
import time

#print("hi")
channel=1
GPIO.setmode (GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
# def callback(channel):
#     print("hi")
#     if GPIO.input (channel):
#         print("no water detected")
#     else:
#         print("water detected")
    
# GPIO.add_event_detect (channel, GPIO.BOTH, bouncetime=300) 
# GPIO.add_event_callback(channel, callback) 

if GPIO.input (channel):
    print("water detected")
else:
    print("no water detected")

# while True:
#     time.sleep(1)

