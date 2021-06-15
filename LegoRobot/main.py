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
        robot = EV3Brick()
        leftMotor = Motor(Port.A)
        rightMotor = Motor(Port.B)
        driveTrain = DriveBase(leftMotor, rightMotor, self.robotContainer.WHEEL_DIAMETER, self.robotContainer.AXEL_TRACK)

        colorSensor = ColorSensor(Port.S1)
        touchSensor = TouchSensor(Port.S2)
        ultrasonicSensor = UltrasonicSensor(Port.S3)

        # variables
        ulSensorRange = 800 #TODO
        colorSensorRange = 100 #TODO

        objectFound = False

        delay = 10

        driveSpeed = 10 #TODO
        turnRate = 10 #TODO

        objectCounter = 0

    def findObject(self):
        self.checkObjectNumber()
        self.driveTrain.drive(0, self.turnRate)
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
            self.dodgeObject()
        elif color == Color.BLACK:
            self.hitObject()

    def hitObject(self):
        self.driveTrain.drive(self.driveSpeed, 0)

        while self.touchSensor.pressed() == False:
            wait(self.delay)
        
        self.driveTrain.stop()
        self.driveTrain.drive(self.driveSpeed, 0)

        while self.pressed() == True:
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
        
    def exit(self):
        print(self.objectCounter)
    
   def checkObjectNumber(self):
       if self.objectCounter > 5:
           self.exit()
       pass


def main():
    r = Robot()
    r.run()

if __name__ == "__main__":
    main()