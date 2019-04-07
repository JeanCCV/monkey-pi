#! /usr/bin/env python
from dobot import Dobot
import time

dobot = Dobot('COM7')

acceleration = 300


dobot.Gripper(208)
dobot.Wait(0.10)

dobot.Gripper(480)
dobot.Wait(0.10)

dobot.MoveWithSpeed(240, 0, 70, acceleration)

dobot.MoveWithSpeed(170, -110, 238, acceleration)


dobot.Gripper(208)
dobot.Wait(0.10)
