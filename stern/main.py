#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftMotor = Motor(Port.A)
rightMotor = Motor(Port.B)

driveTrain = DriveBase(leftMotor, rightMotor, wheel_diameter=55.4, axle_track = 104)

for i in range(7):
    driveTrain.straight(100)
    driveTrain.turn(144)


# Write your program here.
ev3.speaker.beep()
