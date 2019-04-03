#! /usr/bin/env python

from dobot import Dobot
import time

# The top Z to go to.
up = 50
# The bottom Z to go to.
down = 50
# Maximum speed in mm/s
speed = 400
# Acceleration in mm/s^2
acceleration = 300

dobot = Dobot('COM7',debug=False)


# dobot.MoveWithSpeed(210.9, 0, 238, acceleration)

# dobot.MoveWithSpeed(135, 0, 100, acceleration)


while True:
	try:
		dobot.MoveWithSpeed(210.9, 150, 238, acceleration)
		dobot.MoveWithSpeed(0, 150, 238, 50, acceleration)
		dobot.MoveWithSpeed(210.9, 150, 238, acceleration)

		dobot.MoveWithSpeed(210.9, 0, 238, acceleration)

		dobot.MoveWithSpeed(210.9, -150, 238, acceleration)
		dobot.MoveWithSpeed(0, -150, 238, 50, acceleration)
		dobot.MoveWithSpeed(210.9, -150, 238, acceleration)

		dobot.MoveWithSpeed(210.9, 0, 180, acceleration)
		dobot.MoveWithSpeed(240, 0, 180, acceleration)

	finally:
		dobot.MoveWithSpeed(210.9, 0, 238,  acceleration)

# dobot.MoveWithSpeed(50.90000000000002, 0, 78.0, speed, acceleration)