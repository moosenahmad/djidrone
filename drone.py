from djitellopy import Tello
import cv2
import time


tello = Tello()

tello.connect()

cmd = raw_input("What would you like to do?\n")

while cmd != 'q':
	if cmd == "t":
		tello.takeoff()
	elif cmd == 'l':
		tello.move_left(50)
	elif cmd == 'r':
		tello.move_right(50)
	elif cmd == '45':
		tello.rotate_counter_clockwise(45)
	else:
		tello.land()
	cmd = raw_input("Next cmd\n")


tello.land()
tello.end()
