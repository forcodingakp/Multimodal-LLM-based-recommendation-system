from picamera import PiCamera
import time
# Open the file
with open('num.txt', 'r') as f:
    # Write to the file
    curr=int(f.read().strip())

# Open the file
with open('num.txt', 'w') as f:
    # Write to the file
    f.write(str(curr+1))

camera = PiCamera()
camera.start_preview()
time.sleep(3)
camera.capture('/home/pi/Desktop/image%.jpg' % curr)
camera.stop_preview()