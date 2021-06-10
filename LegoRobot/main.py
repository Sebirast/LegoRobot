#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# classes

class Robot:
    def __init__(self):
        robot = ev3Brick()
        leftMotor = Motor(A)
        rightMotor = Motor(B)
        driveTrain = DriveBase

        colorSensor = ColorSensor(S1)
        touchSensor = TouchSensor(S2)
        ultrasonicSensor = UltrasonicSensor(S3)

        robot.addPart(gear)
        robot.addPart(colorSensor.lightSensor)
        robot.addPart(touchSensor)
        robot.addPart(ultrasonicSensor)

    def findObject(self):
        pass

    def goToObject(self):
        pass

    def getColor(self):
        pass

    def hitObject(self):
        pass
    
    def run():
        pass

# variables
ultraSonicSensorRange = 80

def main():
    r = Robot()
    r.run()

if __name__ == "__main__":
    main()