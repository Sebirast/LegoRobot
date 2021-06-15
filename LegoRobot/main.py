#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import RobotContainer

# classes
class Robot:
    def __init__(self):
        self.robotContainer = RobotContainer.RobotContainer()
        self.robot = EV3Brick()
        self.leftMotor = Motor(Port.A)
        self.rightMotor = Motor(Port.B)
        self.driveTrain = DriveBase(self.leftMotor, self.rightMotor, self.robotContainer.WHEEL_DIAMETER, self.robotContainer.AXEL_TRACK)

        self.colorSensor = ColorSensor(Port.S1)
        self.touchSensor = TouchSensor(Port.S2)
        self.ultrasonicSensor = UltrasonicSensor(Port.S3)

        # variables
        self.ulSensorRange = 800  # TODO
        self.colorSensorRange = 100  # TODO

        self.objectFound = False

        self.delay = 10

        self.driveSpeed = 10  # TODO
        self.turnRate = 10  # TODO

        self.objectCounter = 0

    def findObject(self):
        self.checkObjectNumber()
        self.driveTrain.drive(0, self.turnRate)
        distance = self.ultrasonicSensor.distance()

        while distance < self.ulSensorRange:
            currentTraveledAngle = self.driveTrain.angle()
            if currentTraveledAngle > 360:
                self.driveTrain.reset()
                self.goToNewPlace()
            wait(self.delay)

        self.goToObject()

    def goToObject(self):
        self.objectFound = True

        self.driveTrain.drive(100, 0)
        distance = self.ultrasonicSensor.distance(True)
        oldDistance = distance

        while distance > self.colorSensorRange:
            if oldDistance > distance:
                self.driveTrain.stop()
                self.findObject()

            distance = self.ultrasonicSensor.distance(True)
            wait(self.delay)
            oldDistance = distance
        
        self.driveTrain.stop()

        self.getColor()

    def getColor(self):
        color = self.colorSensor.color()
        if color == Color.BLUE or color == Color.BLACK or color == None:
            self.goToNewPlace()

        elif color == Color.BLACK:
            self.hitObject()

    def hitObject(self):
        self.driveTrain.drive(self.driveSpeed, 0)

        while not self.touchSensor.pressed():
            wait(self.delay)
        
        self.driveTrain.stop()
        self.driveTrain.drive(self.driveSpeed, 0)

        while self.touchSensor.pressed():
            wait(self.delay)
        
        self.objectCounter += 1
        self.goToNewPlace()

    def goToNewPlace(self):
        self.driveTrain.straight(-100)
        self.driveTrain.turn(60)
        self.driveTrain.straight(300)
        self.findObject()
    
    def run(self):
        self.findObject()

    def exitProgram(self):
        print(self.objectCounter)
        exit()

    def checkObjectNumber(self):
       if self.objectCounter > 5:
           self.exitProgram()
       pass


def main():
    r = Robot()
    r.run()


if __name__ == "__main__":
    main()