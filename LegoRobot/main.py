#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# classes
WHEEL_DIAMETER = 55.4
AXEL_TRACK = 104
    
class LegoRobot:
    def __init__(self):
        self.robot = EV3Brick()
        self.leftMotor = Motor(Port.A)
        self.rightMotor = Motor(Port.B)
        self.driveTrain = DriveBase(self.leftMotor, self.rightMotor, wheel_diameter = WHEEL_DIAMETER,  axle_track = AXEL_TRACK)

        self.colorSensor = ColorSensor(Port.S1)
        self.touchSensor = TouchSensor(Port.S2)
        self.ultrasonicSensor = UltrasonicSensor(Port.S3)

        # variables
        self.ulSensorRange = 20  # TODO
        self.colorSensorRange = 100  # TODO

        self.objectFound = False

        self.delay = 10

        self.driveSpeed = 100  # TODO
        self.turnRate = 5  # TODO

        self.objectCounter = 0

    def findObject(self):
        print("entered findObjet method")
        self.checkObjectNumber()
        self.driveTrain.drive(100, self.turnRate)
        distance = self.ultrasonicSensor.distance()

        self.driveTrain.reset()

        while distance < self.ulSensorRange:
            # currentTraveledAngle = self.driveTrain.angle()
            distance = self.ultrasonicSensor.distance()
            print(distance)

            # if currentTraveledAngle > 360:
            #     self.driveTrain.reset()
            #     self.goToNewPlace()
            wait(self.delay)

        self.goToObject()


    def goToObject(self):
        print("entered goToObject method")
        self.objectFound = True

        self.driveTrain.drive(self.driveSpeed, 0)
        distance = self.ultrasonicSensor.distance(True)
        oldDistance = distance

        while distance > self.colorSensorRange:
            # if oldDistance > distance:
            #     self.driveTrain.stop()
            #     self.findObject()

            distance = self.ultrasonicSensor.distance(True)
            oldDistance = distance
            wait(self.delay)
        
        self.driveTrain.stop()

        self.getColor()


    def getColor(self):
        print("entered getColor method")
        color = self.colorSensor.color()
        if color == Color.BLUE or color == Color.BLACK or color == None or color == Color.YELLOW:
            self.goToNewPlace()

        elif color == Color.BLACK:
            self.hitObject()


    def hitObject(self):
        print("entered hitObjectMethdo")
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
        print("entered goToNewPlace")
        self.driveTrain.straight(-20)
        self.driveTrain.turn(60)
        self.driveTrain.straight(30)
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

r = LegoRobot()
r.run()